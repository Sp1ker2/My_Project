from sqlalchemy.sql.annotation import Annotated

from core.models import db_helper
from core.security import verify_token
from crud import users as user_crud
from fastapi import APIRouter, Depends, HTTPException
from core.schemas.user import UserCreate, UserLogin, UserRead
from crud.users import create_user, login_user, get_user_by_username
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.security import OAuth2PasswordBearer


# from core.config import ApiV1Prefix as v1
router = APIRouter(tags=["users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.get("", response_model=list[UserRead], responses={404: {"description": "Not found"}})
async def get_users(session: Annotated[AsyncSession] = Depends(db_helper.session_getter)):
    users = await user_crud.get_all_users(session=session)
    return users


@router.post("",
             response_model=UserRead,
             responses={404: {"description": "Not found"}})
async def create_user(user_create: UserCreate,
                      session: Annotated[AsyncSession]
                      = Depends(db_helper.session_getter)
                      ):
    user = await user_crud.create_user(
        session=session,
        user_create=user_create)
    return user


# @router.post("/", response_model=UserRead)
# async def create_user(
#         user_create: UserCreate,
#         session: Annotated[AsyncSession] = Depends(db_helper.session_getter)
# ):
#     user = await user_crud.create_user(session=session, user_create=user_create)
#     return user

#
# @router.post("/register", response_model=UserRead)
# async def register_user(user_create: UserCreate, session: AsyncSession = Depends(db_helper.session_getter)):
#     return await create_user(user_create, session)
#
# @router.post("/login")
# async def login(user_login: UserLogin, session: AsyncSession = Depends(db_helper.session_getter)):
#     return await login_user(user_login.username, user_login.password, session)
#
# @router.get("/me", response_model=UserRead)
# async def get_current_user(token: str = Depends(oauth2_scheme), session: AsyncSession = Depends(db_helper.session_getter)):
#     payload = verify_token(token)
#     if payload is None:
#         raise HTTPException(status_code=401, detail="Invalid or expired token")
#     user = await get_user_by_username(session, payload["sub"])
#     if user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user