import logging

logger = logging.getLogger(__name__)

def record_expense(bot, message, conn):
    expense_data = message.text.strip().split()
    if len(expense_data) != 2:
        bot.reply_to(message, "Please enter expenses in the format '{how_much} {what_I_bought}'.")
        return
    
    try:
        amount = float(expense_data[0])
        description = expense_data[1]

        logger.info(f"(amount, description): {(amount,description)}")

        bot.reply_to(message, "Expense recorded successfully!")
    except ValueError:
        bot.reply_to(message, "Invalid expense amount. Please enter a valid number.")
    except Exception as e:
        logger.error("Error recording expense: %s", str(e))
        bot.reply_to(message, "An error occurred while recording the expense. Please try again later.")
