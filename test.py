import asyncio
import io
import logging
import config
from strings import HELP_COMMAND, HELP_TEXT, reminders_start, reminders_stop, reminders_state, reminders_make, ReminderState
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text
# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.TG_TOKEN)
  dp = Dispatcher(bot)


# команда \help
@dp.message_handler(commands=[HELP_COMMAND])
async def cmd_help_on(message: types.Message):
   await message.answer(HELP_TEXT)


# МОДУЛЬ 1. Команды для напоминаний
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# переменные для хранения состояния включенности уведомлений для Trello и Google Calendar
# @todo #3 исправить этот костыль в будущем
is_schedule_reminder = False
IS_HOMEWORK_REMINDER = False
