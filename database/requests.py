from database.models import async_session
from database.models import User, Game
from sqlalchemy import select, update
from services.convector import matrix_to_json
from services.generator import generate_bot_field


async def set_user(tg_id, user_name: str, name: str):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))
        if not user:
            user = User(tg_id=tg_id, user_name=user_name, name=name)
            session.add(user)
            await session.commit()


async def set_game(tg_id, player_field: list[list[int]], player_ships: list[list[int]]) -> bool:
    async with async_session() as session:
        game = await session.scalar(select(Game).where(Game.tg_id == tg_id))
        bot_field_json = matrix_to_json(generate_bot_field())
        player_field_json = matrix_to_json(player_field)
        player_ships_json = matrix_to_json(player_ships)
        if not game:
            game = Game(tg_id=tg_id,
                        is_in_game=True,
                        player_field=player_field_json,
                        player_ships=player_ships_json,
                        bot_field=bot_field_json)
            session.add(game)
            await session.commit()
            return True
        else:
            return False

async def set_player_field(tg_id, player_field: list[list[int]]):
    async with async_session() as session:
        player_field_json = matrix_to_json(player_field)
        await session.execute(update(Game).where(Game.tg_id == tg_id).values(player_field = player_field_json))
        await session.commit()

async def get_game(tg_id):
    async with async_session() as session:
        return await session.scalar(select(Game).where(Game.tg_id == tg_id))
