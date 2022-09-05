from aiogram import types
from aiogram.types import ReplyKeyboardRemove

from keyboards import commands_default_keyboard
from keyboards import info_default_keyboard
from keyboards import start_callback, navigation_callback
from keyboards import start_inline_keyboard, get_item_inline_keyboard
from loader import dp, data_manager, bot


@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text=f'Здравствуй {message.from_user.first_name}'
                              f'\nты здесь не случайно,'
                              f'\n Я - молодой кофебот,буду рассказывать про кофе!'
                              f'\n а Ты почитай, тут много интересного',
                         reply_markup=start_inline_keyboard)


@dp.callback_query_handler(start_callback.filter())
async def answer_help_command(call: types.CallbackQuery):
    await call.message.answer(text='смотри какая клавиатура',
                              reply_markup=commands_default_keyboard)
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)


@dp.message_handler(commands=['item'])
async def answer_item_command(message: types.Message):
    status, item_info = data_manager.get_item(0)
    item_text = f'Название марки кофе {item_info["name"]}:' \
                f'\nсредняя цена: {item_info["count"]}' \
                f'\nОписание: {item_info["description"]}'
    await message.answer(text=item_text,
                         reply_markup=get_item_inline_keyboard())


@dp.callback_query_handler(navigation_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    id = call.data.split(':')[-1]
    status, item_info = data_manager.get_item(int(id))
    item_text = f'Название марки кофе {item_info["name"]}:' \
                f'\nсредняя цена: {item_info["count"]}' \
                f'\nОписание: {item_info["description"]}'
    await bot.edit_message_text(text=item_text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id)
    await bot.edit_message_reply_markup(reply_markup=get_item_inline_keyboard(id, status),
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)

@dp.message_handler(commands=['history'])
async def answer_item_command(message: types.Message):
    await message.answer(text='Давай кое-что расскажу:',
                            reply_markup=info_default_keyboard)



@dp.message_handler(text=['/История происхождения самого кофе'])
async def answer_item_command(message: types.Message):
        await message.answer(text='Родина кофе — Эфиопия.'
                                  f'\n Итак, история кофе восходит к Абиссинии 10-го века,'
                                  f'\n а это в настоящее время Эфиопия, '
                                  f'\n где впервые были обнаружены кофейные зерна и их основной атрибут кофеин.'
                                  f'\n Но только в 13 веке кофе впервые был обжарен, '
                                  f'\n что позволило ему стать культурным'
                                  f'\n и экономическим продуктом арабской культуры.',
                            reply_markup=info_default_keyboard)

@dp.message_handler(text=['/Что такое капучино?'])
async def answer_item_command(message: types.Message):
        await message.answer(text='Капучи́но — кофейный напиток итальянской кухни'
                                  f'\n на основе эспрессо с добавлением в него '
                                  f'\n подогретого вспененного молока.',
                            reply_markup = info_default_keyboard)

@dp.message_handler(text=['/Что такое раф?'])
async def answer_item_command(message: types.Message):
        await message.answer(text='Раф кофе – это взбитая в капучинаторе смесь из '
                                  'чёрного кофе и сливок, приправленная ванильным сахаром.'
                                  ' Чтобы приготовить любые другие сливочно-кофейные напитки,'
                                  ' уже взбитые сливки выкладывают поверх кофе. Главное отличие рафа'
                                  ' – в том, что кофе и сливки сначала соединяют, а затем взбивают в '
                                  'однородную гладкую пену.',
                            reply_markup = info_default_keyboard)

@dp.message_handler(text=['/Что такое латте?'])
async def answer_item_command(message: types.Message):
        await message.answer(text='Ла́тте — кофейный напиток родом из Италии,'
                                  f'\n состоящий из молока и кофе эспрессо'
                                  f'\n Кофе латте — это слоистый коктейль, который состоит из горячего молока'
                                  f'\n готового эспрессо и густой, душистой пены. '
                                  f'\n Это настоящее итальянское изобретение,'
                                  f'\n которое, кстати, переводится как «запятнанное молоко».',
                             reply_markup=info_default_keyboard)

@dp.message_handler(text=['/Что такое эспрессо?'])
async def answer_item_command(message: types.Message):
        await message.answer(text='Если быть кратким и не вдаваться в подробности,'
                                  f'\n то эспрессо это метод при котором через 8-20г молотого '
                                  f'\n и спрессованного зерна пропускают воду 91-95°С  при давлении 9бар.'
                                  f'\n Тем самым мы получаем что-то вроде экстракта кофе '
                                  f'\n (поэтому сам пролив воды через кофе называют "экстракцией").'
                                  f'\n Сам эспрессо состоит из 2 структур: тело и крема.'
                                  f'\n Крема это ароматические масла которое были взбиты давлением воды,'
                                  f'\n а тело это кофеин, кислоты и сахара.',
                             reply_markup=info_default_keyboard)


@dp.message_handler(commands=['add'])
async def answer_item_command(message: types.Message):
    await message.answer(text='здесь будем добавлять рецепты:'
                                  '\n- сюда добавим рецепт капучино'
                                  '\n- сюда добавим рецепт латте'
                                  '\n- сюда добавим рецепт эспрессо'
                                  '\n место для рецепта вакантно')


@dp.message_handler(text=['Скрыть клавиатуру'])
async def answer_start_command(message: types.Message):
    await message.answer(text='давай без клавы)',
                         reply_markup=ReplyKeyboardRemove())
    await message.answer(text='если что, тыкай ниже',
                         reply_markup=start_inline_keyboard)


@dp.message_handler(content_types=['contact'])
async def answer_item_command(message: types.Message):
    print(message)
    if message.from_user.id == message.contact.user_id:
        await message.answer(text='Это твой контакт')
    else:
        await message.answer(text='А это кто?')


@dp.message_handler(content_types='location')
async def answer_get_location(message: types.Message):
    await message.answer(text=f'Координаты: {message.location.latitude}, {message.location.longitude}')
