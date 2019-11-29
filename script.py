import python
from telegram.ext import Updater, CommandHandler
token = '931989944:AAGpaQSgW3KQHKnGll2gJKdGKXiywVPonNI'
updater = Updater(token, use_context=True)
quality = python.airquality()
def start_method(bot, update):
    bot.message.reply_text("Welcome to Our Bot.\n Developer :  @Iman_Sedgh  \n This is a Free Python Script Using BS4 and Python-telegram-bot modules \n Github : https://github.com/iman-sedgh/Air-pollution-Scraping ")
    bot.message.reply_text("To Get Air Quality Index Use /Get")
    print ('new message')

def get_method(bot,update):
    print('get method')
    bot.message.reply_text("Getting Index From {}".format(quality.url))
    index = quality.getairquality()
    print(index)
    bot.message.reply_text("شاخص آلودگی هوای شهر تهران در حال حاضر {}".format(index))
start_command = CommandHandler('start', start_method)
updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(CommandHandler('Get',get_method))

updater.start_polling()


updater.idle()
