from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database import requests as rq
from services.convector import json_to_matrix
from lexicon.lexicon import LEXICON
from callback_factorys.GameCallbackFactory import GameCallbackFactory


async def get_player_field_keyboard(user_id: int) -> InlineKeyboardMarkup:
    array_buttons: list[list[InlineKeyboardButton]] = []
    game = await rq.get_game(user_id)
    if game.player_field:
        player_field = json_to_matrix(game.player_field)
        field_len = len(player_field)
        for i in range(field_len):
            array_buttons.append([])
            for j in range(field_len):
                array_buttons[i].append(InlineKeyboardButton(
                    text=LEXICON[player_field[i][j]],
                    callback_data=GameCallbackFactory(x=i, y=j).pack()
                ))
    return InlineKeyboardMarkup(inline_keyboard=array_buttons)


async def get_bot_field_keyboard(user_id: int) -> InlineKeyboardMarkup:
    array_buttons: list[list[InlineKeyboardButton]] = []
    game = await rq.get_game(user_id)
    if game:
        bot_field = json_to_matrix(game.player_field)
        field_len = len(bot_field)
        for i in range(field_len):
            array_buttons.append([])
            for j in range(field_len):
                array_buttons[i].append(InlineKeyboardButton(
                    text=LEXICON[bot_field[i][j]],
                    callback_data=GameCallbackFactory(x=i, y=j).pack()
                ))
    return InlineKeyboardMarkup(inline_keyboard=array_buttons)
