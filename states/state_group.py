from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State


class Register(StatesGroup):
    fullname = State()
    course = State()
    phone = State()
    confirm = State()