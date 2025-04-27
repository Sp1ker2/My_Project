from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.annotation import Annotated
from core.models import db_helper
from core.schemas.post import PostRead, PostCreate
from crud import posts as posts_crud

router = APIRouter(tags=["posts"])

@router.get("/posts", response_model=list[PostRead], responses={404: {"description": "Not found"}})
async def get_posts(session: Annotated[AsyncSession] = Depends(db_helper.session_getter)):
    posts = await posts_crud.get_all_posts(session=session)
    return posts


@router.post("/posts", response_model=PostRead,
             responses={404: {"description": "Not found"}})
async def create_post(post_create: PostCreate,
                      session: Annotated[AsyncSession]
                      = Depends(db_helper.session_getter)):
    post = await posts_crud.create_post(session=session, post_create=post_create)
    return post
