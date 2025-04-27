from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    username: str
    email: EmailStr
    # foo: int
    # bar:int


class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

    # password:str


class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id: int


