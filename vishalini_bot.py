from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from Adafruit_IO import Client,Data
import os

def turnoff(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Led turned off")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://depositphotos.com/10120309/stock-photo-empty-light-bulb-on-white.html')
  send_value(0)
def turnon(update, context):
  context.bot.send_message(chat_id=update.effective_chat.id, text="Led turned on")
  context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://www.cleanpng.com/png-incandescent-light-bulb-lighting-electricity-clip-684554/')
  send_value(1)

def send_value(value):
  feed = aio.feeds('light')
  aio.send_data(feed.key,value)

def input_message(update, context):
  text=update.message.text
  if text == 'turn on':
    send_value(1)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Led turned on")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://img.icons8.com/plasticine/2x/light-on.png')
  elif text == 'turn off':
    send_value(0)
    context.bot.send_message(chat_id=update.effective_chat.id,text="Led turned off")
    context.bot.send_photo(chat_id=update.effective_chat.id,photo='https://pngimg.com/uploads/bulb/bulb_PNG1241.png')

def start(update,context):
  start_message='''
/turnoff or 'turn off':To turn of the led ,sends value=0 in feed
/turnon or 'turn on'  :To turn on the led ,sends value=1 in feed
'''
  context.bot.send_message(chat_id=update.effective_chat.id, text=start_message)
ADAFRUIT_IO_USERNAME= os.getenvy("ADAFRUIT_IO_USERNAME")
ADAFRUIT_IO_KEY= os.getenvy("ADAFRUIT_IO_KEY")
TOKEN = os.getenv('TOKEN')

from Adafruit_IO import Client, Feed
aio = Client(ADAFRUIT_IO_USERNAME,ADAFRUIT_IO_KEY)
updater=Updater(TOKEN,use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('turnoff',turnoff))
dispatcher.add_handler(CommandHandler('turnon',turnon))
dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command),input_message))
updater.start_polling()
updater.idle()
