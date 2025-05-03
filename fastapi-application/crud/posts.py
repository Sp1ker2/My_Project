from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.models import Post
from core.schemas.post import PostCreate


from sqlalchemy.orm import joinedload

async def get_all_posts(session: AsyncSession):
    stmt = select(Post).options(joinedload(Post.owner)).order_by(Post.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_post(post_create: PostCreate, session: AsyncSession, current_user):
    post_data = post_create.model_dump()
    post_data['owner_id'] = current_user.id  # беремо id з поточного користувача

    new_post = Post(**post_data)

    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)

    return new_post
