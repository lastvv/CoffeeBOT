from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .callback_data import start_callback, navigation_callback


def get_item_inline_keyboard(item_index='0', status='Small') -> InlineKeyboardMarkup:
    item_inline_keyboard = InlineKeyboardMarkup()
    match status:
        case 'Big':
            index_left = str(int(item_index) - 1)
            btm = InlineKeyboardButton(text='<<<',
                                       callback_data=navigation_callback.new(
                                           for_data='items',
                                           id=index_left)
                                       )
            item_inline_keyboard.add(btm)
        case 'Small':
            index_right = str(int(item_index) + 1)
            btm = InlineKeyboardButton(text='>>>',
                                       callback_data=navigation_callback.new(
                                           for_data='items',
                                           id=index_right)
                                       )
            item_inline_keyboard.add(btm)
        case _:
            index_left = str(int(item_index) - 1)
            index_right = str(int(item_index) + 1)
            btm_left = InlineKeyboardButton(text='<<<',
                                            callback_data=navigation_callback.new(
                                                for_data='items',
                                                id=index_left))
            btm_right = InlineKeyboardButton(text='>>>',
                                             callback_data=navigation_callback.new(
                                                 for_data='items',
                                                 id=index_right))
            item_inline_keyboard.row(btm_left, btm_right)

    return item_inline_keyboard


start_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Главное меню',
                             callback_data=start_callback.new())
    ]
])
