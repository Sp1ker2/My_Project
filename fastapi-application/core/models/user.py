from sqlalchemy import UniqueConstraint, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .mixins.int_id_pk import IntIdPkMixin as ipkm
from .base import Base
class User(Base):
    __tablename__ = 'users'
    ipkm.id
    username: Mapped[str] = mapped_column(unique=True)
    # foo:Mapped[int]
    # bar:Mapped[int]
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)
    posts = relationship("Post", back_populates="owner")


    # __table_args__ = (UniqueConstraint("foo","bar"),)
    def __repr__(self):
        return f"<User(username={self.username})>"
    def __str__(self):
        return self.username
