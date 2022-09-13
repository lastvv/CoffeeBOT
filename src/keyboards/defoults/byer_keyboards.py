from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/marki')
        ],
        [
            KeyboardButton(text='/history'),
            KeyboardButton(text='/add')
        ],
        [
            KeyboardButton(text='Поделиться контактом',
                           request_contact=True)
        ],
        [
            KeyboardButton(text='Скрыть клавиатуру')
        ]
    ],
    resize_keyboard=True
)


see_commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Показать')
        ]
    ],
    resize_keyboard=True
)
info_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='[.История происхождения самого кофе.]')
        ],
        [
            KeyboardButton(text='[Что такое капучино?]')
        ],
        [
            KeyboardButton(text='[История происхождения капучино]')
        ],
        [
            KeyboardButton(text='[Что такое латте?]')
        ],
        [
            KeyboardButton(text='[История происхождения латте]')
        ],
        [
            KeyboardButton(text='[Что такое эспрессо?]')
        ],
        [
            KeyboardButton(text='[История происхождения эспрессо]')
        ],
        [
            KeyboardButton(text='[Что такое раф?]')
        ],
        [
            KeyboardButton(text='[История происхождения раф]')
        ],
        [
            KeyboardButton(text='-номер телефона сюда давай-',
                           request_contact=True),
            KeyboardButton(text='--где ты есть?--',
                           request_location=True)
        ],
        [
            KeyboardButton(text='Показать')
        ]
    ],
    resize_keyboard=True
)






# access_btm = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Подтвердить номер телефона',
#                            request_contact=True)
#         ]
#     ],
#     resize_keyboard=True
# )
