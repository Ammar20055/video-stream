""" inline section button """

from config import BOT_USERNAME
from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="π π²π»π π±οΈ", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="ππΉπΌππ² ποΈ", url=f'https://t.me/{BOT_USERNAME}?startgroup=true'),
    ],
    [
      InlineKeyboardButton("ππ΅π π²π± ππΉπ‘πΎπ¬π―β’β β€Ά", callback_data="ahmedelnqyb")
    ]
  ]
  return buttons


def menu_markup(user_id):
  buttons = [
        [
            InlineKeyboardButton("π£ππ¨π¦π βΈ", callback_data=f'cbpause | {user_id}'),
            InlineKeyboardButton("π₯ππ¦π¨π π  βΆοΈ", callback_data=f'cbresume | {user_id}')
        ],
        [
            InlineKeyboardButton("ππ‘π βΉ", callback_data=f'cbstop | {user_id}')
        ],
        [
            InlineKeyboardButton("ππ΅π π²π± ππΉπ‘πΎπ¬π―β’β β€Ά", callback_data="ahmedelnqyb")
        ]
    ]
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "ππΉπΌππ² ποΈ", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "π Go Back", callback_data="cbmenu"
      )
    ]
  ]
)
