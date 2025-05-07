from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from .mixins.int_id_pk import IntIdPkMixin
from core.models import Base


class Likes(Base,IntIdPkMixin):
    __tablename__ = "likes"
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    __table_args__ = (UniqueConstraint("user_id", "post_id", name="unique_like"),)

