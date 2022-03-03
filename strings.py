from enum import Enum
from aiogram.utils.markdown import text, bold


HELP_COMMAND = 'help'
HELP_TEXT = text('**Это помощь :D**')


class ReminderState(Enum):
    R_FALSE = 'Не нуждается в изменении'
    R_DO = 'За изменения взялся'
    R_TRUE = 'Нужно изменить'

    def __init__(self, description):
        self.description = description


class Reminder:
    def __init__(self, command, description):
        self.command = command
        self.description = description


# @todo #3 перевести в Enum
reminders_start = {
    'schedule': Reminder('schedule', text(f"Необходимо внести изменения в {bold('Google Calendar')}.",
                                          "Данное сообщение будет повторяться каждые 15 минут.",
                                          "Для отключения необходимо ввести /done_schedule.", sep='\n')),
    'homework': Reminder('homework', text("Необходимо внести изменения в Trello.",
                                          "Данное сообщение будет повторяться каждые 15 минут.",
                                          "Для отключения необходимо ввести /done_homework", sep='\n'))
}


reminders_state = {
    'schedule': Reminder('is_schedule', "Состояние Google Calendar:"),
    'homework': Reminder('is_homework', "Состояние Trello:")
}


reminders_make = {
    'schedule': Reminder('make_schedule', "За внесения поправок в Google Calendar взялся - "),
    'homework': Reminder('make_homework', "За внесения изменений в Trello взялся - ")
}


reminders_stop = {
    'schedule': Reminder('done_schedule', text("Google Calendar:",
                                               "Повтор напоминаний отключен.", sep='\n')),
    'homework': Reminder('done_homework', text("Trello:",
                                               "Повтор напоминаний отключен.", sep='\n'))
}
