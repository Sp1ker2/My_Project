from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username:str
    email:EmailStr
    foo: int
    bar:int
class UserCreate(UserBase):
    # password:str
    pass
class UserRead(UserBase):
    model_config = ConfigDict(
        from_attributes=True
    )
    id:int
