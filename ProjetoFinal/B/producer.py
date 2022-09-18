import json
import time
import random

from kafka import KafkaProducer
from dotenv import dotenv_values

config = dotenv_values(".env")

import logging

from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

producer = KafkaProducer(
        value_serializer=lambda m: json.dumps(m).encode('utf-8'),
        bootstrap_servers=['localhost:9092']
    )

def check_politician(sentence):
    if 'bolsonaro' in sentence:
        return 'Bolsonaro'
    elif 'lula' in sentence:
        return 'Lula'

# -------------- Telegram --------------

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    msg_content = update.message.text
    msg_id = update.message.message_id
    msg = {'message': msg_content.lower(), 'id': msg_id, 'politician': check_politician(msg_content.lower())}
    print(msg)
    producer.send('mensagens', msg)


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(config['TOKEN'])

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

# -------------- Random --------------

# msgs = [
#     'eu te odeio bolsonaro',
#     'eu te odeio lula',
#     'bolsonaro é bom',
#     'lula é bom',
# ]

# id = 0

# while True:
#     msg = random.choice(msgs)
#     msg = {'message': msg, 'politician': check_politician(msg), 'id': id}
#     producer.send('mensagens', msg)
#     time.sleep(1)
#     id += 1