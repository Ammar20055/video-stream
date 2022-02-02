""" inline section button """

from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)


def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="𝗠𝗲𝗻𝘂 🖱️", callback_data=f'cbmenu | {user_id}'),
      InlineKeyboardButton(text="𝗖𝗹𝗼𝘀𝗲 🗑️", callback_data=f'cls'),
    ],
    [
      InlineKeyboardButton("𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", callback_data="ahmedelnqyb")
    ]
  ]
  return buttons


def menu_markup(user_id):
  buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("𝗣𝗔𝗨𝗦𝗘 ⏸", callback_data=f'cbpause | {user_id}'),
            InlineKeyboardButton("𝗥𝗘𝗦𝗨𝗠𝗘  ▶️", callback_data=f'cbresume | {user_id}')
        ],
        [
            InlineKeyboardButton("𝗘𝗡𝗗 ⏹", callback_data=f'cbstop | {user_id}')
        ],
        [
            InlineKeyboardButton("𝗔𝗵𝗠𝗲𝗱 𝗘𝗹𝗡𝗾𝗬𝗯™★ ⤶", callback_data="ahmedelnqyb")
        ]
    ]
   )
  return buttons


close_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "𝗖𝗹𝗼𝘀𝗲 🗑️", callback_data="cls"
      )
    ]
  ]
)


back_mark = InlineKeyboardMarkup(
  [
    [
      InlineKeyboardButton(
        "🔙 Go Back", callback_data="cbmenu"
      )
    ]
  ]
)
