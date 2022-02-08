from aiogram import Bot, Dispatcher, executor, types
import config
import logging
from strings import help_command, help_text


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.TG_TOKEN)
dp = Dispatcher(bot)


# команда \help
@dp.message_handler(commands=[help_command])
async def cmd_reminder_on(message: types.Message):
    await message.answer(help_text)


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
