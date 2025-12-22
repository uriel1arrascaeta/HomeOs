from pydantic import BaseModel, EmailStr, Field
from models import UserRole
# Este modelo define cómo debe ser el cuerpo (body) de la petición de login.
# FastAPI lo usará para validar automáticamente que la petición entrante es correcta.


class LoginRequest(BaseModel):
    email: EmailStr  # Cambiamos 'username' por 'email' para mayor claridad
    password: str

# Este modelo define la estructura de la respuesta que enviaremos
# cuando el login sea exitoso. Coincide con lo que el frontend espera.


class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    first_name: str

# Esquema para la creación de un usuario.
# Incluye la contraseña, que se recibirá en la petición.


class UserCreate(BaseModel):
    email: EmailStr
    first_name: str
    # La contraseña debe tener entre 8 y 72 caracteres.
    # Bcrypt tiene un límite de 72 bytes.
    password: str = Field(min_length=8, max_length=72)
    role: UserRole

# Esquema para devolver los datos de un usuario.
# NO incluye la contraseña por seguridad.


class UserOut(BaseModel):
    id: int
    email: EmailStr
    first_name: str
    role: UserRole

# Esquema para la respuesta del perfil de usuario.
# Anidamos el esquema UserOut para mantener la estructura.


class Profile(BaseModel):
    user: UserOut
    avatar: str | None = None  # El avatar puede ser opcional

    class Config:
        from_attributes = True
