def handle_start_command(bot, message):
    bot.reply_to(message, "Welcome to Expense Tracker Bot!\n"
                              "Send your expenses in the format '{amount} {description}'.")
