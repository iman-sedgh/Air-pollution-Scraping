import scraper
import logging
from uuid import uuid4
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import InlineQueryHandler
from telegram import InputTextMessageContent
from telegram import InlineQueryResultArticle

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

token = '931989944:AAGpaQSgW3KQHKnGll2gJKdGKXiywVPonNI' #air quality
#token = '422767920:AAEZVBVBYoCrWu4Pula_eccUiYDcn5FPCq0' #iman iot prj bot

updater = Updater(token, use_context=True)
quality = scraper.airquality()
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

def inline_feature(bot,update):
    query = bot.inline_query.query
    results = []
    results.append(InlineQueryResultArticle(id = uuid4(),title="English",input_message_content = InputTextMessageContent("Air Quality Index Of Tehran Is {}".format(str(quality.getairquality())))))
    results.append(InlineQueryResultArticle(id = uuid4(),title="Persian",input_message_content = InputTextMessageContent("شاخص آلودگی هوای تهران در حال حاضر {}".format(str(quality.getairquality())))))
    if query.find('{}') != -1:
        results.append(InlineQueryResultArticle(id = uuid4(),title="Custom Text",input_message_content = InputTextMessageContent(query.format(("<b>" +quality.getairquality() + "</b>")),parse_mode='HTML')))
    else :
        results.append(InlineQueryResultArticle(id = uuid4(),title="Custom Text",description='*Error !!!*' ,input_message_content = InputTextMessageContent ("* Error \n {} Not Found !!*",parse_mode='Markdown')))
    bot.inline_query.answer(results)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


start_command = CommandHandler('start', start_method)
get_command = CommandHandler('get',get_method)
index_inline = InlineQueryHandler(inline_feature)
updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(get_command)
updater.dispatcher.add_handler(index_inline)
updater.dispatcher.add_error_handler(error)
import threading
t1 = threading.Thread(target=updater.start_polling, args = () )
t2 = threading.Thread(target=quality.threadfunc, args = () )
t1.start()
t2.start()
#updater.start_polling()


updater.idle()
