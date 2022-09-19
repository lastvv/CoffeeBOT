from aiogram.dispatcher.filters.state import StatesGroup, State

class ByerState(StatesGroup):
    wait_item_name = State()