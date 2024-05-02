from aiogram import Router
from aiogram.types import Message

rt = Router()


# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@rt.message()
async def send_echo(message: Message):
    await message.answer(f'Такой команды у меня нету!')