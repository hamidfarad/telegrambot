from telegram import Update, Bot
from telegram.ext import Updater
from telegram.ext import CommandHandler,MessageHandler,Filters
import os
PORT = int(os.environ.get('PORT', 5000))

def start (update , context):
    context.bot.send_message(chat_id=update.message.chat.id, text="I'm a bot, please talk to me!")
    print(update.message.chat.id)

updater = Updater("1429548938:AAGFez9aLIvodiAxpRtxJsMVskFsMdpUt34")

updater.dispatcher.add_handler(CommandHandler('start' , start))

TOKEN = "1429548938:AAGFez9aLIvodiAxpRtxJsMVskFsMdpUt34"
updater.start_webhook(listen="0.0.0.0",port=int(PORT),url_path=TOKEN)
updater.bot.setWebhook('https://powerful-gorge-46204.herokuapp.com/' + TOKEN)
updater.idle()