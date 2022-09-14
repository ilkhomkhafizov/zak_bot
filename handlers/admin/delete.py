from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsPrivate
from loader import dp
from utils.check_admin import check_admin
from utils.db_api import question_commands
from utils.misc import rate_limit


@rate_limit(limit=12, key='/delete')
@dp.message_handler(IsPrivate(), Command('delete'))
@check_admin
async def delete_command(message: types.Message):
    questions = await question_commands.select_all_questions()
    if len(questions) > 0:
        for question in questions:
            await question.delete()
        await message.answer('Savollar o\'chirildi')
    else:
        await message.answer('Savollar hali yuq')
