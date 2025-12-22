from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # URL de conexión a la base de datos
    DATABASE_URL: str

    # Configuración de JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Esta línea le dice a Pydantic que cargue las variables desde un archivo .env
    model_config = SettingsConfigDict(env_file=".env")


# Creamos una única instancia que importaremos en otros módulos
settings = Settings()
