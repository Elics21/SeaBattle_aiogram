from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon import LEXICON

command_start_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text=LEXICON["new_game_btn"], callback_data="new_game")]
])