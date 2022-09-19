from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram.utils.markdown import hbold, hunderline, hitalic

from keyboards import commands_default_keyboard
from keyboards import info_default_keyboard
from keyboards import start_callback, navigation_callback
from keyboards import start_inline_keyboard, get_item_inline_keyboard
from loader import dp, data_manager, bot
from states import ByerState


@dp.message_handler(text=['Привет', 'Начать'])
@dp.message_handler(commands='start')
async def answer_start_command(message: types.Message):
    await message.answer(text=f'{hunderline("Здравствуй")}, {hbold(message.from_user.first_name)}👋'
                              f'\n{hitalic("ты здесь не случайно")}'
                              f'\n Я - молодой кофебот,🙂буду рассказывать про кофе!'
                              f'\n а Ты почитай, тут много интересного😉',
                         reply_markup=start_inline_keyboard)


@dp.message_handler(text=['Найти марку'])
async def get_item_name(message: types.Message):
    await message.answer(text='Какую марку ты хочешь найти?')
    await ByerState.wait_item_name.set()


@dp.callback_query_handler(start_callback.filter())
async def answer_help_command(call: types.CallbackQuery):
    await call.message.answer(text='смотри какая клавиатура👀',
                              reply_markup=commands_default_keyboard)
    await bot.delete_message(chat_id=call.message.chat.id,
                             message_id=call.message.message_id)


@dp.message_handler(commands=['marki'])
async def answer_item_command(message: types.Message):
    status, item_info = data_manager.get_item(0)
    item_text = f'Название марки кофе {item_info["name"]}:' \
                f'\nсредняя цена: {item_info["count"]}' \
                f'\nОписание: {item_info["description"]}'
    await message.answer(text=item_text,
                         reply_markup=get_item_inline_keyboard())
    data = {
        'item_info_in_data': item_info
    }

@dp.message_handler(text=['Найти марку'])
async def get_item_name(message: types.Message):
    await message.answer(text='вот тебе список:'
                              'f\n 1.Нескафе')
    await ByerState.wait_item_name.set()


@dp.message_handler(state=ByerState.wait_item_name)
async def get_item_command(message: types.Message, state: FSMContext):
    item_info = data_manager.search_item_by_name(message.text)
    if not item_info:
        pass
    else:
        item_index, item_info = item_info[0]
        await message.answer(text=f'Название марки кофе {item_info["name"]}:' \
                                  f'\nсредняя цена: {item_info["count"]}' \
                                  f'\nОписание: {item_info["description"]}')

        data = {
            'item_info_in_data': item_info
        }
        await state.update_data(item_info_in_data=item_info)
    await state.reset_state()


@dp.callback_query_handler(navigation_callback.filter(for_data='items'))
async def see_new_item(call: types.CallbackQuery):
    id = call.data.split(':')[-1]
    status, item_info = data_manager.get_item(int(id))
    item_text = f'Название марки кофе {item_info["name"]}:' \
                f'\nсредняя цена за кг в зёрнах: {item_info["count"]}' \
                f'\nОписание: {item_info["description"]}'
    await bot.edit_message_text(text=item_text,
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id)
    await bot.edit_message_reply_markup(reply_markup=get_item_inline_keyboard(id, status),
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id)


@dp.message_handler(commands=['history'])
async def answer_item_command(message: types.Message):
    await message.answer(text='Давай кое-что расскажу про кофе:',
                         reply_markup=info_default_keyboard)


@dp.message_handler(text=['[.История происхождения самого кофе.]'])
async def answer_item_command(message: types.Message):
    await message.answer(text='📂Родина кофе — Эфиопия.'
                              f'\n Итак, история кофе восходит к Абиссинии 10-го века,'
                              f'\n а это в настоящее время Эфиопия, '
                              f'\n где впервые были обнаружены кофейные зерна и их основной атрибут кофеин.'
                              f'\n Но только в 13 веке кофе впервые был обжарен, '
                              f'\n что позволило ему стать культурным'
                              f'\n и экономическим продуктом арабской культуры.',
                         reply_markup=info_default_keyboard)


@dp.message_handler(text=['[Что такое капучино?]'])
async def answer_item_command(message: types.Message):
    await message.answer(text='📂Капучи́но — кофейный напиток итальянской кухни'
                              f'\n на основе эспрессо с добавлением в него '
                              f'\n подогретого вспененного молока.',
                         reply_markup=info_default_keyboard)


@dp.message_handler(text=['[История происхождения латте]'])
async def answer_item_command(message: types.Message):
    await message.answer(text='📂Латте, как ни странно, изобрели итальянские домохозяйки.'
                              ' Когда-то семья итальянцев в полном составе садилась за'
                              ' стол и начинала завтракать. Взрослые пили натуральный черный кофе,'
                              ' а чтобы дети чувствовали себя наравне со взрослыми, им в напиток наливали'
                              ' горячее молоко, тем самым понизив концентрацию кофеина. Детский кофе'
                              ' получался немного запятнанным, поэтому его назвали «запятнанное молоко», '
                              ' что на итальянском звучит как «латте».',
                         reply_markup=info_default_keyboard)


@dp.message_handler(text=['[История происхождения капучино]'])
async def answer_item_command(message: types.Message):
    await message.answer(text='📂Название этого напитка связывают различными'
                              ' путями с монахами-капуцинами.'
                              'По одной из версий служители церкви любили насладиться '
                              'кофейным вкусом и ароматом. Однако употребление кофе не '
                              'приветствовалось среди религиозных представителей, так как'
                              'он считался напитком дьявола. И чтобы не отказываться от '
                              'удовольствия, монахи придумали смешивать черный кофе с молоком',
                         reply_markup=info_default_keyboard)


@dp.message_handler(text=['[История происхождения эспрессо]'])
async def answer_item_command(message: types.Message):
    await message.answer(text='📂В Италии очень любят и ценят крепкий чёрный кофе,'
                              ' приготовленный из хороших зёрен. До начала 20 века'
                              ' готовили любимый бодрящий напиток только в турках, '
                              'что не всегда было практично, ведь приходилось ждать '
                              'пока он закипит. А представьте, если вы торопитесь и '
                              'забежали в кофейню за чашечкой крепкого кофе, то всё '
                              'равно придётся ждать, пока вам его приготовят и сварят. '
                              'Это подтолкнуло одного миланского инженера-изобретателя'
                              ' Луиджи Беццера к созданию аппарата, который будет сам '
                              'готовить кофе. В 1901 году он представил свою первую кофемашину.'
                              ' Практичность, удобство и скорость приготовления, были оценены '
                              'по достоинству. Почти сразу же лицензия на это изобретение была'
                              ' куплена предпринимателем Дезидерио Павони. После чего он запустил'
                              ' производство и стал выпускать кофемашину Pavoni, которая появилась'
                              ' в продаже в 1905 году.',
                         reply_markup=info_default_keyboard)


@dp.message_handler(text=['[Что такое раф?]'])
async def answer_item_command(message: types.Message):
    await message.answer(text='📂Раф кофе – это взбитая в капучинаторе смесь из '
                              'чёрного кофе и сливок, приправленная ванильным сахаром.'
                              ' Чтобы приготовить любые другие сливочно-кофейные напитки,'
                              ' уже взбитые сливки выкладывают поверх кофе. Главное отличие рафа'
                              ' – в том, что кофе и сливки сначала соединяют, а затем взбивают в '
                              'однородную гладкую пену.',
                         reply_markup=info_default_keyboard)


@dp.message_handler(text=['[История происхождения раф]'])
async def answer_item_command(message: types.Message):
    await message.answer(text='📂1996-7 год. Маленький кофейный магазин '
                              'рядом с метро Кузнецкий мост (Кофе Бин). '
                              'Три десятка сортов кофе в зерне, кофеварка '
                              'эспрессо. В общем, культурный шок для того времени.'
                              'Что такое капучино, в Москве узнают года через четыре'
                              '. Работали по трое, один старший – открыть\закрыть магазин, '
                              'касса и пр. Всё остальное – вместе.Было очень интересно, '
                              'много нового, и многое зависело от нас. Постоянные гости со'
                              ' своими привычками и пожеланиями.Один из них (Рафаэль или Раф)'
                              ' наш кофе не пил, а мы так гордились своими творениями. Специально '
                              'для него стали взбивать вместе кофе +сливки 11%+ванильный сахар. Его'
                              ' многочисленные друзья начали просить “кофе как Рафу”, первое время '
                              'так и называли “как Рафу”. Затем упростили до “Раф кофе”'
                              'Сейчас этот рецепт известен по всей стране, правда,к сожалению '
                              'иногда меняют оригинальное название.',
                         reply_markup=info_default_keyboard)


@dp.message_handler(text=['[Что такое латте?]'])
async def answer_item_command(message: types.Message):
    await message.answer(text='📂Ла́тте — кофейный напиток родом из Италии,'
                              ' состоящий из молока и кофе эспрессо Кофе латте — это слоистый коктейль,'
                              ' который состоит из горячего молока готового эспрессо и густой, душистой'
                              ' пены.Это настоящее итальянское изобретение,которое, кстати, переводится'
                              ' как «запятнанное молоко».',
                         reply_markup=info_default_keyboard)


@dp.message_handler(text=['[Что такое эспрессо?]'])
async def answer_item_command(message: types.Message):
    await message.answer(text='📂Если быть кратким и не вдаваться в подробности,'
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


@dp.message_handler(text=['Показать'])
async def answer_start_command(message: types.Message):
    await message.answer(text='Показать👇',
                         reply_markup=start_inline_keyboard)


@dp.message_handler(content_types=['contact'])
async def answer_item_command(message: types.Message):
    print(message)
    if message.from_user.id == message.contact.user_id:
        await message.answer(text='Мы вам перезвоним')
    else:
        await message.answer(text='А это кто?')


@dp.message_handler(content_types='location')
async def answer_get_location(message: types.Message):
    await message.answer(text=f'Координаты: {message.location.latitude}, {message.location.longitude}')
