from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import logging
import re

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am a calculator bot. Send me a mathematical expression to evaluate.')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Send me any mathematical expression, and I will calculate the result for you.')

def evaluate_expression(expression):
    """Evaluate a mathematical expression."""
    try:
        # Only allow numbers and basic operators
        if re.match(r'^[\d+\-*/. ()]+$', expression):
            # Evaluate the expression safely
            result = eval(expression)
            return result
        else:
            return "Invalid expression"
    except Exception as e:
        return str(e)

def handle_message(update, context):
    """Handle incoming messages and calculate the result."""
    text = update.message.text
    result = evaluate_expression(text)
    update.message.reply_text(result)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Get the bot token from @BotFather
    token = 'AAHyaDIDREyuFgZdaTELpaLlJl9NHOIHS_c'

    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - handle the message on Telegram
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()