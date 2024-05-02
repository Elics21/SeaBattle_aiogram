from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

from lexicon.lexicon import LEXICON
from keyboards.basic_kb import command_start_kb
from database.requests import set_user

rt = Router()

@rt.message(CommandStart())
async def command_start(m: Message):
    await set_user(m.from_user.id, m.from_user.username, m.from_user.first_name)
    await m.answer(LEXICON["/start"], reply_markup=command_start_kb)