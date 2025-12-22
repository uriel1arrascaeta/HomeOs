from sqlalchemy import Boolean, Column, Integer, String, Enum as SQLAlchemyEnum
from database import Base
import enum

# Usamos un Enum de Python para definir los roles, igual que en Django


class UserRole(str, enum.Enum):
    buyer = "buyer"
    agent = "agent"
    admin = "admin"


class User(Base):
    # El nombre de la tabla debe coincidir con el que Django creó
    __tablename__ = "accounts_customuser"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String, nullable=False)
    # Django guarda el hash en el campo 'password'
    password = Column(String, nullable=False)
    role = Column(SQLAlchemyEnum(UserRole), nullable=False)
    is_active = Column(Boolean, default=True)
