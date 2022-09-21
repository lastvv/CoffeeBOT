from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware


class GetDBUser(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        data['User'] = (message.from_user.id, message.from_user.username, 'та самая информация')

    async def on_process_callback_quare(self,call: types,CallbackQuery,data: dict):
        data['User_on_callback'] = 'User_fron_callback'