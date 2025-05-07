from pydantic import BaseModel, ConfigDict


class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    pass


class PostAuthor(BaseModel):
    username: str
    model_config = ConfigDict(from_attributes=True)


class PostRead(PostBase):
    id: int
    like: int = 0
    owner: PostAuthor
    model_config = ConfigDict(from_attributes=True)
