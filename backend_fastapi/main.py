from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# Importamos los módulos que acabamos de crear
import auth
import schemas
import models
import crud
from database import SessionLocal, engine, get_db

# Esto crea las tablas en la base de datos si no existen.
# En un entorno de producción, se suele gestionar con herramientas de migración como Alembic.
models.Base.metadata.create_all(bind=engine)

# Creamos una instancia de la aplicación FastAPI
app = FastAPI()

# --- Configuración de CORS ---
# Orígenes permitidos (tu frontend de React)
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todas las cabeceras
)


@app.post("/api/v1/accounts/register/", response_model=schemas.UserOut)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Verificamos si ya existe un usuario con ese email
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe un usuario con este email",
        )
    # Creamos el usuario usando nuestra función del CRUD
    return crud.create_user(db=db, user=user)


@app.post("/api/v1/accounts/login/", response_model=schemas.Token)
async def login_for_access_token(form_data: schemas.LoginRequest, db: Session = Depends(get_db)):
    # Buscamos al usuario en la base de datos por su email
    user = crud.get_user_by_email(db, email=form_data.email)

    # Django guarda las contraseñas con un formato que passlib no puede verificar directamente.
    # Por ahora, asumiremos que las contraseñas se hashean con bcrypt.
    # Si el login falla para usuarios existentes, necesitaremos ajustar el verificador de contraseñas.
    if not user or not auth.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = auth.create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer", "role": user.role, "first_name": user.first_name}


@app.get("/api/v1/accounts/profile/", response_model=schemas.Profile)
async def read_users_me(current_user: models.User = Depends(auth.get_current_user)):
    # La dependencia `get_current_user` ya nos da el usuario autenticado.
    # Por ahora, devolvemos un avatar por defecto.
    return {"user": current_user, "avatar": "https://i.pravatar.cc/150"}
