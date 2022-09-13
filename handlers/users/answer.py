from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from loader import dp
from states import Answer
from utils.check_admin import check_auth
from utils.db_api import question_commands, register_commands
from utils.misc import rate_limit


@rate_limit(limit=120, key='/answer')
@dp.message_handler(IsPrivate(), Command('answer'))
@check_auth
async def answer_command(message: types.Message):
    questions = await question_commands.select_all_questions()
    if len(questions) > 0:
        last_question = questions[-1]
        question_text = last_question.question_text
        question_audio = last_question.question_audio
        question_voice = last_question.question_voice
        if question_audio:
            await dp.bot.send_audio(chat_id=message.chat.id, audio=question_audio, caption=question_text)
        else:
            await dp.bot.send_voice(chat_id=message.chat.id, voice=question_voice, caption=question_text)
        await message.answer('Javobni kiriting')
        await Answer.state.set()
    else:
        await message.answer('Savollar hali yuq')


@dp.message_handler(IsPrivate(), state=Answer.state)
async def answer_send_command(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(state=answer)
    text = f'Javobingiz qabul qilindi \n' \
           f'Rahmat!!!'
    await register_commands.update_answer(user_id=message.from_user.id, answer=answer)

    await state.finish()
    await message.answer(text)
