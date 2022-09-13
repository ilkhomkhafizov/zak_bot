from aiogram.dispatcher.filters.state import StatesGroup, State


class User(StatesGroup):
    full_name = State()
    address = State()
    phone = State()
