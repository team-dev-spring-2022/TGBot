from aiogram import Bot, Dispatcher, executor, types
import config
import logging
import asyncio
from strings import help_command, help_text, reminders_start


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.TG_TOKEN)
dp = Dispatcher(bot)


# команда \help
@dp.message_handler(commands=[help_command])
async def cmd_reminder_on(message: types.Message):
    await message.answer(help_text)


# МОДУЛЬ 1. Команды для напоминаний
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# переменные для хранения состояния включенности уведомлений для Trello и Google Calendar
# @todo #3 исправить этот костыль в будущем
is_schedule_reminder = False
is_homework_reminder = False


# Команды активации цикличного напоминания для Google Calendar и Trello.
# @todo #3 сделать ассинхронными потоками без глобальных переменных
@dp.message_handler(commands=[reminders_start['schedule'].command, reminders_start['homework'].command])
async def cmd_reminder_on(message: types.Message):
    if message.get_command(pure=True) == reminders_start['schedule'].command:
        global is_schedule_reminder
        if is_schedule_reminder:
            await message.answer('Уже включено')
            return
        await message.answer(reminders_start['schedule'].description)
        is_schedule_reminder = True
        while is_schedule_reminder:
            await asyncio.sleep(config.REMINDER_TIMER)
            if is_schedule_reminder:
                await message.answer(reminders_start['schedule'].description)
    elif message.get_command(pure=True) == reminders_start['homework'].command:
        global is_homework_reminder
        if is_homework_reminder:
            await message.answer('Уже включено')
            return
        await message.answer(reminders_start['homework'].description)
        is_homework_reminder = True
        while is_homework_reminder:
            await asyncio.sleep(config.REMINDER_TIMER)
            if is_homework_reminder:
                await message.answer(reminders_start['homework'].description)


# @todo #3 сделать команды для завершения цикличного таймера напоминаний для Google Calendar и Trello


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
