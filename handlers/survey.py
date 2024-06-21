import datetime
import re
from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import database

survey_router = Router()

class BookSurvey(StatesGroup):
    name = State()
    phone = State()
    visit_date = State()
    food_quality = State()
    cleanliness = State()
    comments = State()

@survey_router.callback_query(F.data == "survey")
async def start_survey(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(BookSurvey.name)
    await callback_query.message.answer("как вас зовут?")

@survey_router.message(BookSurvey.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text.strip()
    if re.fullmatch(r'[A-Za-zА-Яа-яЁё]+', name):
        await state.update_data(name=name)
        await state.set_state(BookSurvey.phone)
        await message.answer("Ваш номер телефона?")
    else:
        await message.answer("Пожалуйста, введите только имя, без пробелов и специальных символов.")

@survey_router.message(BookSurvey.phone)
async def process_phone(message: types.Message, state: FSMContext):
    phone = message.text.strip()
    if re.fullmatch(r'\+?\d{10,15}', phone):  # Adjust regex based on expected phone number formats
        await state.update_data(phone=phone)
        await state.set_state(BookSurvey.visit_date)
        await message.answer("дата вашего посещения в формате ДД.ММ.ГГГГ:")
    else:
        await message.answer("Пожалуйста, введите действующий телефонный номер.")

@survey_router.message(BookSurvey.visit_date)
async def process_visit_date(message: types.Message, state: FSMContext):
    try:
        visit_date = datetime.datetime.strptime(message.text, "%d.%m.%Y")
        await state.update_data(visit_date=visit_date)
        await state.set_state(BookSurvey.food_quality)
        await message.answer("оцените качество еды от 1 до 5")
    except ValueError:
        await message.answer("Неверный формат даты. Пожалуйста, введите дату в формате ДД.ММ.ГГГГ:")

@survey_router.message(BookSurvey.food_quality)
async def process_food_quality(message: types.Message, state: FSMContext):
    try:
        quality_rating = int(message.text)
        if 1 <= quality_rating <= 5:
            await state.update_data(food_quality=quality_rating)
            await state.set_state(BookSurvey.cleanliness)
            await message.answer("Пожалуйста, введите число от 1 до 5 для оценки чистоты заведения:")
        else:
            await message.answer("Пожалуйста, введите число от 1 до 5 для оценки качества еды:")
    except ValueError:
        await message.answer("Пожалуйста, введите число от 1 до 5 для оценки качества еды:")

@survey_router.message(BookSurvey.cleanliness)
async def process_cleanliness(message: types.Message, state: FSMContext):
    try:
        cleanliness_rating = int(message.text)
        if 1 <= cleanliness_rating <= 5:
            await state.update_data(cleanliness=cleanliness_rating)
            await state.set_state(BookSurvey.comments)
            await message.answer("Ваши дополнительные комментарии")
        else:
            await message.answer("Пожалуйста, введите число от 1 до 5 для оценки чистоты заведения:")
    except ValueError:
        await message.answer("Пожалуйста, введите число от 1 до 5 для оценки чистоты заведения:")

@survey_router.message(BookSurvey.comments)
async def process_comments(message: types.Message, state: FSMContext):
    comments = message.text.strip()
    await state.update_data(comments=comments)
    data = await state.get_data()
    await database.execute(" INSERT INTO survey_results (name, phone, visit_date, food_quality, cleanliness, comments)   VALUES (?, ?, ?, ?, ?, ?)",
        (data['name'], data['phone'], data['visit_date'], data['food_quality'], data['cleanliness'], data['comments'])
    )
    await message.answer("Спасибо за прохождения опроса")
    await state.finish()
