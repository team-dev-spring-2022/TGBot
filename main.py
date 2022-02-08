import logging
from aiogram import Bot, Dispatcher, executor
import config


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.TG_TOKEN)
dp = Dispatcher(bot)


# команда \help
# @todo #2 сделать команду help


# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
