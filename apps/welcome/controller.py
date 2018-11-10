import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
level=logging.DEBUG)

logger = logging.getLogger(__name__)

def start(bot, update):
    text_start = "Bot"
    bot.send_message(chat_id=update.message.chat_id, text=text_start)


def cancel(bot, update):
    text_cancel = "Permintaan di cancel"
    bot.send_message(chat_id=update.message.chat_id, text=text_cancel)