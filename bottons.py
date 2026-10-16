from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup

async def main_buttons():
    mar = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text= "maktab darsliklari"),
            ],
            [
                KeyboardButton(text=" IT kurslari"),
                KeyboardButton(text="IELTS Course")
            ],
            [
                KeyboardButton(text="Send Lacation",request_location=True),
                KeyboardButton(text="Send contact",request_contact=True)
            ]
        ],
        resize_keyboard=True
    )
    return mar

async def school_buttons():
    buttons = []
    for i in range(1,5):
        buttons.append([KeyboardButton(text = f"{i}-sinf darsliklari")])
    buttons.append([KeyboardButton(text="Go Back")])
    return ReplyKeyboardMarkup(keyboard=buttons,resize_keyboard=True)

async def it_buttons():
    buttons = [
        [
            KeyboardButton(text="Dasturlash boyicha qolanma")
        ],
        [
            KeyboardButton(text="Go Back")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons,resize_keyboard=True)

async def coder_buttons():
    inline_keybrd = InlineKeyboardMarkup(
        inline_keyboard =[
                [
                    InlineKeyboardButton(text="'C' dasturlash",callback_data="C"),
                    InlineKeyboardButton(text="Python dasturlash",callback_data="Python")
                ],
                [
                    InlineKeyboardButton(text="C++",callback_data="C++"),
                    InlineKeyboardButton(text="Java",callback_data="Java")
                ]
            ]
    )
    return inline_keybrd