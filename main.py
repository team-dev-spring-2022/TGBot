import asyncio
import io
import logging
from aiogram import Bot, Dispatcher, executor, types
import config
from strings import HELP_COMMAND, HELP_TEXT, reminders_start, reminders_stop


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
IS_SCHEDULE_REMINDER = False
IS_HOMEWORK_REMINDER = False
FILE_NAME = ''


# Команды активации цикличного напоминания для Google Calendar и Trello.
# @todo #3 сделать ассинхронными потоками без глобальных переменных
@dp.message_handler(commands=[reminders_start['schedule'].command, reminders_start['homework'].command])
async def cmd_reminder_on(message: types.Message):
    if message.get_command(pure=True) == reminders_start['schedule'].command:
        global IS_SCHEDULE_REMINDER
        if IS_SCHEDULE_REMINDER:
            await message.answer('Уже включено')
            return
        await message.answer(reminders_start['schedule'].description)
        IS_SCHEDULE_REMINDER = True
        while IS_SCHEDULE_REMINDER:
            await asyncio.sleep(config.REMINDER_TIMER)
            if IS_SCHEDULE_REMINDER:
                await message.answer(reminders_start['schedule'].description)
    elif message.get_command(pure=True) == reminders_start['homework'].command:
        global IS_HOMEWORK_REMINDER
        if IS_HOMEWORK_REMINDER:
            await message.answer('Уже включено')
            return
        await message.answer(reminders_start['homework'].description)
        IS_HOMEWORK_REMINDER = True
        while IS_HOMEWORK_REMINDER:
            await asyncio.sleep(config.REMINDER_TIMER)
            if IS_HOMEWORK_REMINDER:
                await message.answer(reminders_start['homework'].description)


@dp.message_handler(commands=[reminders_stop['schedule'].command, reminders_stop['homework'].command])
async def cmd_reminder_off(message: types.Message):
    if message.get_command(pure=True) == reminders_stop['schedule'].command:
        global IS_SCHEDULE_REMINDER, file_name
        if not IS_SCHEDULE_REMINDER:
            await message.answer("Напоминание в Google Calendar не включено")
            return
        IS_SCHEDULE_REMINDER = False
        await message.answer(reminders_stop['schedule'].description)
        file_name = 'responsible_in_schedule.txt'
    elif message.get_command(pure=True) == reminders_stop['homework'].command:
        global IS_HOMEWORK_REMINDER
        if not IS_HOMEWORK_REMINDER:
            await message.answer("Напоминание в Trello не включено")
            return
        IS_HOMEWORK_REMINDER = False
        await message.answer(reminders_stop['homework'].description)
        file_name = 'responsible_in_homework.txt'
    with io.open(file_name, 'w', encoding='utf8') as text_file:
        print(file=text_file)

# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
