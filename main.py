import config
import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import text


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.TG_TOKEN)
dp = Dispatcher(bot)


# команда \help
# @todo сделать команду help


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
