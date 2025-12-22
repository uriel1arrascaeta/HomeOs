from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# Usamos la URL de la base de datos desde nuestra configuración centralizada
engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependencia de FastAPI para obtener una sesión de BD por petición


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
