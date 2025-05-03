from datetime import datetime, timedelta
from core.models.db_helper import DatabaseHelper as dh, DatabaseHelper
from core.models import db_helper
from crud import users as user_crud
from fastapi import APIRouter, Depends, HTTPException
from core.schemas.user import UserCreate, UserLogin, UserRead
from crud.users import create_user, login_user, get_user_by_username, ban_user, unban_user
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer
from typing import List

# from core.config import ApiV1Prefix as v1
router = APIRouter(tags=["users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Правильное использование session_getter
async def get_session(db_helper: DatabaseHelper = Depends(lambda: db_helper)) -> AsyncSession:
    async for session in db_helper.session_getter():
        yield session

# Маршрут для бана пользователя
@router.post("/ban_user")
async def ban_user(username: str, ban_duration: int, session: AsyncSession = Depends(get_session)):
    user = await get_user_by_username(username, session)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.is_banned_until and user.is_banned_until > datetime.now():
        raise HTTPException(status_code=403, detail=f"User is already banned until {user.is_banned_until}")

    user.is_banned_until = datetime.now() + timedelta(minutes=ban_duration)
    user.ban_count += 1
    session.add(user)

    try:
        await session.commit()
        await session.refresh(user)
        return {"message": f"User {username} has been banned for {ban_duration} minutes."}
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))

# Маршрут для разбана пользователя
@router.post("/unban_user/")
async def unban_user_endpoint(username: str, session: AsyncSession = Depends(get_session)):
    return await unban_user(username, session)

# Получение всех пользователей
@router.get("", response_model=List[UserRead], responses={404: {"description": "Not found"}})
async def get_users(session: AsyncSession = Depends(get_session)):
    users = await user_crud.get_all_users(session=session)
    return users

# Создание пользователя
@router.post("",
             response_model=UserRead,
             responses={404: {"description": "Not found"}})
async def create_user_endpoint(user_create: UserCreate,
                                session: AsyncSession = Depends(get_session)
                                ):
    user = await user_crud.create_user(session=session, user_create=user_create)
    return user
