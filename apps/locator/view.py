import logging
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ConversationHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.DEBUG)

logger = logging.getLogger(__name__)

NAME, RESULT = range(2)

def location(bot, update):
    logger.debug('data {}'.format(update))
    update.message.reply_text(update.message.location.longitude)

    return NAME

def name(bot, update):
    user = update.message.from_user

    logger.debug("location User in => {}".format(user_data))
    update.message.reply_text("testing")

    return ConversationHandler.END


def end(bot, update):
    user = update.message.from_user
    logger.info("user %s cancel conversation ", user.first_name)
    update.message.reply_text('Terima Kasih',reply_markup=ReplyKeyboardRemove)

    return ConversationHandler.END