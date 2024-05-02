from aiogram import Router, F
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import Message, CallbackQuery
import json
from aiogram.filters import Command

from keyboards.game_kb import get_player_field_keyboard, get_bot_field_keyboard
from lexicon.lexicon import LEXICON
from database import requests as rq
from callback_factorys.GameCallbackFactory import GameCallbackFactory
from services import convector

rt = Router()

field: list[list[int]] = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

ships: list[list[int]] = [
    [1, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0]
]


@rt.callback_query(F.data == "new_game")
async def process_new_game(cl: CallbackQuery):
    flag: bool = await rq.set_game(cl.from_user.id, field, ships)
    if flag:
        await cl.message.edit_text(text="Товое поле:",
                                   reply_markup=await get_player_field_keyboard(cl.from_user.id))
    else:
        await cl.message.edit_text("Вы уже в игре!\n\nЗакончите игру, чтобы начать новую.",
                                   reply_markup=await get_player_field_keyboard(cl.from_user.id))
    await cl.answer()


@rt.callback_query(GameCallbackFactory.filter())
async def process_btn_press(callback: CallbackQuery, callback_data: GameCallbackFactory):
    game = await rq.get_game(callback.from_user.id)
    player_field = convector.json_to_matrix(game.player_field)
    player_ships = convector.json_to_matrix(game.player_ships)
    if player_field[callback_data.x][callback_data.y] == 0 and \
            player_ships[callback_data.x][callback_data.y] == 0:
        answer = LEXICON['miss']
        player_field[callback_data.x][callback_data.y] = 1
    elif field[callback_data.x][callback_data.y] == 0 and \
            player_ships[callback_data.x][callback_data.y] == 1:
        answer = LEXICON['hit']
        player_field[callback_data.x][callback_data.y] = 2
    else:
        answer = LEXICON['used']

    try:

        await rq.set_player_field(tg_id=callback.from_user.id,
                                  player_field=player_field)
        await callback.message.edit_text(
            text=LEXICON['next_move'],
            reply_markup=await get_player_field_keyboard(callback.from_user.id))
    except TelegramBadRequest:
        pass

    await callback.answer(answer)

