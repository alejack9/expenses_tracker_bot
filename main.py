from logger_bootstrapper import logger
import os
import telebot
from commands_container_register import register_commands

logger.debug(f"bot_token: {os.environ.get('BOT_TOKEN')}")
bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

# Call the register_commands function to register command handlers
register_commands(bot)

def main():
    bot.polling()

if __name__ == '__main__':
    main()
