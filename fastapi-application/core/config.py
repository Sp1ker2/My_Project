from pydantic_settings import BaseSettings
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
class Settings(BaseSettings):
    run:RunConfig = RunConfig()
    # prefix
    api: ApiPrefix= ApiPrefix()
    # db
    db: DatabaseConfig

settings = Settings()