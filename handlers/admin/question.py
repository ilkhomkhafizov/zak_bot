from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp
from filters import IsPrivate
from states import Question
from utils.check_admin import check_admin
from utils.db_api import question_commands as commands


@dp.message_handler(IsPrivate(), text='/question')
@check_admin
async def question_command(message: types.Message):
    await message.answer(f"Savol matnini kiriting!")
    await Question.question_text.set()


@dp.message_handler(IsPrivate(), state=Question.question_text)
async def question_text_command(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Audio fayl orqali savol kiritish',
                                                               callback_data='question_audio'),
                                          InlineKeyboardButton(text='Ovozli habar orqali savol kiritish',
                                                               callback_data='question_voice')
                                      ]
                                  ])
    await state.update_data(question_text=answer)
    await message.answer("Quyidagi menu-dan birini tanlang", reply_markup=markup)
    await Question.state.set()


@dp.callback_query_handler(text='question_audio', state=Question.state)
async def add_question_audio(call: types.CallbackQuery):
    await call.message.answer("Audio fayl orqali savolni yuklang")
    await Question.question_audio.set()


@dp.message_handler(IsPrivate(), state=Question.question_audio, content_types=types.ContentTypes.AUDIO)
async def add_audio(message: types.Message, state: FSMContext):
    audio_id = message.audio.file_id
    await state.update_data(question_audio=audio_id)
    data = await state.get_data()
    text = data.get('question_text')
    audio = data.get('question_audio')
    await commands.add_question(question_text=text, question_audio=audio)
    await state.finish()
    await message.answer("Savol yuklanildi!")


@dp.callback_query_handler(text='question_voice', state=Question.state)
async def add_question_voice(call: types.CallbackQuery):
    await call.message.answer("Ovozli habar orqali savolni yuklang")
    await Question.question_voice.set()


@dp.message_handler(IsPrivate(), state=Question.question_voice, content_types=types.ContentTypes.VOICE)
async def add_audio(message: types.Message, state: FSMContext):
    voice_id = message.voice.file_id
    await state.update_data(question_voice=voice_id)
    data = await state.get_data()
    text = data.get('question_text')
    voice = data.get('question_voice')
    await commands.add_question(question_text=text, question_voice=voice)
    await state.finish()
    await message.answer("Savol yuklanildi!")
