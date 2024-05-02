from database.models import async_session
from database.models import User, Game
from sqlalchemy import select
from services.to_json import matrix_to_json


async def set_user(tg_id, user_name: str, name: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            user = User(tg_id=tg_id, user_name=user_name, name=name)
            session.add(user)
            await session.commit()


async def set_game(tg_id, plaer_field: list[list[int]]) -> bool:
    async with async_session() as session:
        game = await session.scalar(select(Game).where(Game.tg_id == tg_id))
        plaer_field_json = matrix_to_json(plaer_field)
        if not game:
            game = Game(tg_id=tg_id, is_in_game=True, plaer_field=plaer_field_json)
            session.add(game)
            await session.commit()
            return True
        else:
            return False
