from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from lexicon.lexicon import LEXICON

rt = Router()

@rt.callback_query(F.data == "new_game")
async def process_new_game(cl: CallbackQuery):
    await cl.message.edit_text("Игра ничинается!")
