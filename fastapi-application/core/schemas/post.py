from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(BaseModel):
    title: str
    content: str
    # user_id: int

class PostAuthor(BaseModel):
    username: str

    class Config:
        from_attributes = True
class PostRead(PostBase):
    id: int
    title: str
    content: str
    owner: PostAuthor
model_config = ConfigDict(
        from_attributes=True
    )
