from aiogram.filters.callback_data import CallbackData


class GameCallbackFactory(CallbackData, prefix='game'):
    x: int
    y: int