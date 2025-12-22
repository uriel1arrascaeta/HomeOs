from sqlalchemy.orm import Session
import models
import schemas
import auth


def get_user_by_email(db: Session, email: str):
    """Busca y devuelve un usuario por su email."""
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    """Crea un nuevo usuario en la base de datos."""
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(email=user.email, first_name=user.first_name,
                          password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
