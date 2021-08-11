import logging
import os

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, dispatcher

# Activate logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Define commands handler
def start(update: Update, context: CallbackContext):
    """ Send a message when the command /start is issued. """
    user = update.effective_user
    logger.info("user: {}".format(user.username))
    update.message.reply_markdown_v2(fr'Hi {user.mention_markdown_v2()}\!',
                                     reply_markup=ForceReply(selective=True))

def echo(update: Update, context: CallbackContext):
    """ Echo the user message. """
    update.message.reply_text(update.message.text)

## Init main bot
def main():
    """ Start the bot """
    telegram_token = os.environ.get('TELEGRAM_TOKEN')
    # Create the updater
    updater = Updater(telegram_token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on differents commands - answer in Telegram:
    dispatcher.add_handler(CommandHandler("start", start))
    
    # non command message 
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()


    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == "__main__":
    main()