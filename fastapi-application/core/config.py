from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import BaseModel,PostgresDsn
import os
from datetime import timedelta

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-key")
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 час

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users : str = "/users"
    posts : str = "/posts"
class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()
class DatabaseConfig(BaseModel):
    # host: str = "localhost"
    # port: int = 5432
    url: PostgresDsn
    echo : bool = False
    echo_pool : bool = False
    max_overflow : int = 10
    pool_size : int = 50
    naming_convention: dict[str, str] = {
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_N_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template",".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",

        )
    # database_config = DatabaseConfig()
    run:RunConfig = RunConfig()
    # prefix
    api: ApiPrefix= ApiPrefix()
    # db
    db: DatabaseConfig

settings = Settings()