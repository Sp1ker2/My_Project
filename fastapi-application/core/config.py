from pydantic_settings import BaseSettings
from pydantic import BaseModel
class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000
class ApiPrefix(BaseModel):
    prefix: str = "/api"
class Settings(BaseSettings):
    run:RunConfig = RunConfig()
    # prefix
    api: ApiPrefix= ApiPrefix()

settings = Settings()