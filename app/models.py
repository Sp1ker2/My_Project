from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

post_tags = Table('post_tags', Base.metadata,
                  Column('post_id', ForeignKey('posts.id'), primary_key=True),
                  Column('tag_id', ForeignKey('tags.id'), primary_key=True)
                  )


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    author_id = Column(Integer, ForeignKey('authors.id'))
    category_id = Column(Integer, ForeignKey('categories.id'))
    tags = relationship('Tag', secondary=post_tags, back_populates='posts')
    author = relationship('Author')
    category = relationship('Category')


Tag.posts = relationship('Post', secondary=post_tags, back_populates='tags')
