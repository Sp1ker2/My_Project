from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

# ----------------------
# Роли пользователей
# ----------------------
class UserRole(str, Enum):
    ADMIN = "ADMIN"
    TEAM = "TEAM"
    CALL = "CALL"


# ----------------------
# Схемы для пользователей
# ----------------------
class UserBase(BaseModel):
    id: Optional[int] = None
    username: str
    role: UserRole
    team_id: Optional[int] = None  # Для TEAM и CALL

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    username: str
    password: str
    role: Optional[UserRole] = UserRole.CALL
    team_id: Optional[int] = None


class UserCreateBase(BaseModel):
    username: str
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        from_attributes = True


# ----------------------
# Схемы для команд
# ----------------------
class TeamBase(BaseModel):
    name: str


class TeamOut(TeamBase):
    id: int

    class Config:
        from_attributes = True


class TeamWithLeadCreate(BaseModel):
    team_name: str
    lead: UserCreateBase  # Лидер команды (TEAM)


# ----------------------
# Схемы для клиентов
# ----------------------
class ClientStatus(str, Enum):
    NEW = "NEW"
    IN_WORK = "IN WORK"
    CLOSED = "CLOSED"
    DEAD = "DEAD"
    STUCK = "STUCK"


class ClientBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None
    status: ClientStatus = ClientStatus.NEW


class ClientCreate(ClientBase):
    pass


class ClientOut(ClientBase):
    id: int
    team_id: Optional[int] = None  # Привязка к Team-лидеру
    user_id: Optional[int] = None  # Привязка к Call

    class Config:
        from_attributes = True
