from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from config import settings
import crud
import models
from database import get_db
# Le decimos a passlib que entienda tanto bcrypt (para los nuevos usuarios)
# como los hashes de Django (para los usuarios existentes).
# 'bcrypt' será el predeterminado para las nuevas contraseñas.
pwd_context = CryptContext(
    schemes=["bcrypt", "django_pbkdf2_sha256"], deprecated="auto")


# Esta es la URL donde el frontend enviará el email/contraseña para obtener un token.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/accounts/login/")

# --- Funciones de Utilidad ---


def verify_password(plain_password, hashed_password):
    """Verifica una contraseña plana contra su hash usando el contexto unificado de passlib."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Genera el hash de una contraseña usando bcrypt."""
    return pwd_context.hash(password)


def create_access_token(data: dict):
    """Crea un token de acceso JWT."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + \
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Dependencia para obtener el usuario actual a partir de un token JWT.
    Decodifica el token, extrae el email (sub) y busca al usuario en la BD.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudieron validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    return user
