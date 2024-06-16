import datetime
import re
from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


survey_router = Router()

class BookSurvey(StatesGroup):
    name = State()
    numbers = State()
    data = State()
    qualities = State()
    purities = State()
    comments = State()


@survey_router.callback_query(lambda call: call.data =="survey")

async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.name)
    await message.answer("как вас зовут?")


@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()

    if re.fullmatch(r'[A-Za-zА-Яа-яЁё]+', name):
        await state.update_data(name=name)
        await state.set_state(BookSurvey.numbers)
        await message.answer("ваш номер телефона")
    else:
        await message.answer("Пожалуйста, введите только имя, без пробелов и специальных символов.")


@survey_router.message(BookSurvey.numbers)
async def process_data(message: types.Message, state: FSMContext):
    await state.set_state(BookSurvey.data)
    await message.answer("дата вашего посещения в формате ДД.ММ.ГГГГ:")


@survey_router.message(BookSurvey.data)
async def process_date(message: types.Message, state: FSMContext):
    try:

        visit_date = datetime.datetime.strptime(message.text, "%d.%m.%Y")
        await state.update_data(visit_date=visit_date)
        await message.answer("Спасибо! Дата посещения сохранена.")
        await state.set_state(BookSurvey.data)
        await state.set_state(BookSurvey.qualities)
        await message.answer("оцените качество еды от 1 до 5")

    except ValueError:
        await message.answer("Неверный формат даты. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ:")


@survey_router.message(BookSurvey.qualities)
async def process_qualities(message: types.Message, state: FSMContext):
    try:
        quality_rating = int(message.text)
        if 1 <= quality_rating <= 5:
            await state.update_data(quality_rating=quality_rating)
            await state.set_state(BookSurvey.purities)
            await message.answer("Оцените чистоту заведения от 1 до 5:")
        else:
            await message.answer("Пожалуйста, введите число от 1 до 5 для оценки качества еды:")
    except ValueError:
        await message.answer("Пожалуйста, введите число от 1 до 5 для оценки качества еды:")


@survey_router.message(BookSurvey.purities)
async def process_purities(message: types.Message, state: FSMContext):
    try:
        purity_rating = int(message.text)
        if 1 <= purity_rating <= 5:
            await state.update_data(purity_rating=purity_rating)
            await message.answer("Спасибо за ваши ответы!")
            await state.set_state(BookSurvey.purities)
            await state.set_state(BookSurvey.comments)
            await message.answer("Ваши дополнительные комментарии")
        else:
            await message.answer("Пожалуйста, введите число от 1 до 5 для оценки чистоты заведения:")
    except ValueError:
        await message.answer("Пожалуйста, введите число от 1 до 5 для оценки чистоты заведения:")


@survey_router.message(BookSurvey.comments)
async def process_data(message: types.Message, state: FSMContext):
    comments = message.text.strip()
    await state.update_data(comments=comments)

    await message.answer("Спасибо за прохождения опроса")
    await state.finish()






