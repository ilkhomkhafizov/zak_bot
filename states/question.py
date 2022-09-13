from aiogram.dispatcher.filters.state import StatesGroup, State


class Question(StatesGroup):
    question_text = State()
    question_audio = State()
    question_voice = State()
    state = State()
