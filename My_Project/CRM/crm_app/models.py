from enum import Enum as PyEnum
from sqlalchemy import Column, Integer, String, Enum as SqlEnum, Table, ForeignKey
from sqlalchemy.orm import relationship
from crm_app.database import Base


# -------------------------
# Статусы клиента
# -------------------------
class ClientStatus(str, PyEnum):
    NEW = "NEW"
    IN_WORK = "IN WORK"
    CLOSED = "CLOSED"
    DEAD = "DEAD"
    STUCK = "STUCK"


# -------------------------
# Таблица связи клиент ↔ теги
# -------------------------
client_tags = Table(
    "client_tags",
    Base.metadata,
    Column("client_id", Integer, ForeignKey("clients.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


# -------------------------
# Тег
# -------------------------
class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    clients = relationship("Client", secondary=client_tags, back_populates="tags")


# -------------------------
# Роли пользователей
# -------------------------
class UserRole(str, PyEnum):
    ADMIN = "admin"
    TEAM = "team"
    CALL = "call"


# -------------------------
# Админ
# -------------------------
class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    # один админ → много команд
    teams = relationship("Team", back_populates="admin")


# -------------------------
# Команда
# -------------------------
class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    admin_id = Column(Integer, ForeignKey("admins.id"))

    admin = relationship("Admin", back_populates="teams")
    calls = relationship("Call", back_populates="team")
    users = relationship("User", back_populates="team")
    clients = relationship("Client", back_populates="team")


# -------------------------
# Звонки
# -------------------------
class Call(Base):
    __tablename__ = "calls"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)  # spectr / vortyty

    team_id = Column(Integer, ForeignKey("teams.id"))
    team = relationship("Team", back_populates="calls")


# -------------------------
# Клиенты
# -------------------------
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    status = Column(String, nullable=True)

    team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)

    tags = relationship("Tag", secondary=client_tags, back_populates="clients")

    team = relationship("Team", back_populates="clients")
    user = relationship("User", back_populates="clients")


# -------------------------
# Пользователи
# -------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(SqlEnum(UserRole), default=UserRole.CALL)

    team_id = Column(Integer, ForeignKey("teams.id"), nullable=True)

    team = relationship("Team", back_populates="users")
    clients = relationship("Client", back_populates="user")
