from datetime import datetime

from sqlalchemy import UniqueConstraint, String, DateTime, Boolean, Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .mixins.int_id_pk import IntIdPkMixin as ipkm
from .base import Base
class User(ipkm, Base):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    hashed_password: Mapped[str] = mapped_column(String(200), nullable=False)

    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_banned_until: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    ban_count: Mapped[int] = mapped_column(Integer, default=0)

    liked_posts = relationship("Likes", backref="user", cascade="all, delete-orphan")

    posts = relationship("Post", back_populates="owner")

    def __repr__(self):
        return f"<User(username={self.username})>"

    def __str__(self):
        return self.username

    # __table_args__ = (UniqueConstraint("foo","bar"),)

