from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(BaseModel):
    title: str
    content: str
    # user_id: int

class PostRead(PostBase):
    id: int
    model_config = ConfigDict(
        from_attributes=True
    )
