from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import json
from aiogram.filters import Command
from lexicon.lexicon import LEXICON
from database import requests as rq

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
    flag: bool = await rq.set_game(cl.from_user.id, field)
    if(flag):
        await cl.message.edit_text("Игра ничинается!")
    else:
        await cl.message.answer("Вы уже в игре!\n\nЗакончите игру, чтобы начать новую.")

