import logging
from telegram.ext import (Updater, 
    CommandHandler, MessageHandler, Filters, ConversationHandler)

from apps.welcome.controller import start, cancel

from apps.locator.view import location, name, end

from apps.locator.view import NAME, RESULT

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.DEBUG)

logger = logging.getLogger()


def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)


def main():
    
    updater = Updater("TOKEN")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("cancel", cancel))

    # dp.add_handler(MessageHandler(Filters.location, location))

    conversation_user = ConversationHandler(
        entry_points=[MessageHandler(Filters.location, location)],

        states={
            NAME:[MessageHandler(Filters.text, name, pass_user_data=True)]
        },

        fallbacks=[CommandHandler("/stop", end)]
    )

    dp.add_handler(conversation_user)

     # log all errors
    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()