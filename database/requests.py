from database.models import async_session
from database.models import User
from sqlalchemy import select

async def set_user(tg_id, user_name: str, name: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            user = User(tg_id=tg_id, user_name=user_name, name=name)
            session.add(user)
            await session.commit()