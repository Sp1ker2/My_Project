from pydantic_settings import BaseSettings,SettingsConfigDict
from pydantic import BaseModel,PostgresDsn
class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
class ApiPrefix(BaseModel):
    prefix: str = "/api"
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