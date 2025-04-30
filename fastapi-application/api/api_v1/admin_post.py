from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from core.models import Post, User
from core.models.db_helper import db_helper
from core.security import get_current_user

router = APIRouter()

@router.delete("/delete/{post_id}")
async def delete_post(
    post_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(db_helper.session_getter)
):
    # Разрешено удалять посты только "Em Tru" или админу
    if current_user.username != "Em Tru" and not current_user.is_admin:
        raise HTTPException(status_code=403, detail="You do not have permission to delete posts")

    result = await session.execute(select(Post).where(Post.id == post_id))
    post = result.scalar_one_or_none()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    await session.delete(post)
    await session.commit()

    return {"message": f"Post with id {post_id} has been deleted successfully"}
