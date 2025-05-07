from pydantic import BaseModel
from typing import List, Optional

class AuthorBase(BaseModel):
    name: str
    email: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int

    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True

class PostBase(BaseModel):
    title: str
    content: str
    author_id: int
    category_id: int

class PostCreate(PostBase):
    tags: List[int]

class Post(PostBase):
    id: int
    tags: List[Tag]


    class Config:
        from_attributes = True
