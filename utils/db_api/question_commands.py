from asyncpg import UniqueViolationError

from utils.db_api.schemas.question import Question


async def add_question(question_text: str, question_audio=None, question_voice=None):
    try:
        question = Question(question_text=question_text, question_audio=question_audio, question_voice=question_voice)
        await question.create()
    except UniqueViolationError:
        print("Вопрос не добавлен")


async def select_all_questions():
    questions = await Question.query.gino.all()
    return questions


async def select_last_question():
    last_question = await Question.query.gino.last()
    return last_question
