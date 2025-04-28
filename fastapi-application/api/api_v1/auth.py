
from core.models import db_helper
from fastapi import APIRouter, Depends, HTTPException
from core.schemas.user import UserCreate, UserLogin, UserRead
from crud.users import create_user, login_user, get_user_by_username
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/register", response_model=UserRead)
async def register_user(user_create: UserCreate, session: AsyncSession = Depends(db_helper.session_getter)):
    return await create_user(user_create, session)

from fastapi import Form

@router.post("/login")
async def login(
    username: str = Form(...),
    password: str = Form(...),
    session: AsyncSession = Depends(db_helper.session_getter),
):
    return await login_user(username, password, session)
