from logger_bootstrapper import logger
import os
import telebot
import psycopg2
from commands_container_register import register_commands

logger.debug(f"bot_token: {os.environ.get('BOT_TOKEN')}")
bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))
conn = psycopg2.connect(database=os.environ.get('POSTGRES_DB'),
                        host=os.environ.get('POSTGRES_HOST'),
                        user=os.environ.get('POSTGRES_USER'),
                        password=os.environ.get('POSTGRES_PASSWORD'))

# Call the register_commands function to register command handlers
register_commands(bot, conn)

def main():
    bot.polling()

if __name__ == '__main__':
    main()
