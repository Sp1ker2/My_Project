from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from .mixins.int_id_pk import IntIdPkMixin as ipkm
from .base import Base
class User(Base):
    ipkm.id
    username: Mapped[str] = mapped_column(unique=True)
    foo:Mapped[int]
    bar:Mapped[int]
    email: Mapped[str] = mapped_column(unique=True)
    __table_args__ = (UniqueConstraint("foo","bar"),)
    def __repr__(self):
        return f"<User(username={self.username})>"
    def __str__(self):
        return self.username
