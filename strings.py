from aiogram.utils.markdown import text, bold

help_command = 'help'
help_text = text('**Это помощь :D**')


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