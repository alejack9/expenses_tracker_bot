from telebot.types import Message
from commands.start import handle_start_command
from commands.expense import record_expense

def register_commands(bot, connection):
    @bot.message_handler(commands=['start'])
    def start_handler(message: Message):
        handle_start_command(bot, message)

    @bot.message_handler(func=lambda message: True)
    def expense_handler(message: Message):
        record_expense(bot, message, connection)
