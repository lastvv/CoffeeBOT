from aiogram import Dispatcher
from .database_mdl import GetDBUser


def setup(dp: Dispatcher):
    dp.middleware.setup(GetDBUser())
