from art import tprint
from loader import bot
from loguru import logger
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import apiai, json


if __name__ == "__main__":
    tprint('bot', font='block', chr_ignore=True)
    logger.add('debug_file', format='{time} {level} {message}', level='DEBUG', rotation='6:00', compression='zip')

    updater = Updater(token='5787437579:AAGJFPuoLlpvTKoip7SiOytTrygj1qF4Xgo')  # Токен API к Telegram
    dispatcher = updater.dispatcher

    def startCommand(bot, update):
        bot.send_message(chat_id=update.message.chat_id, text='Привет, давай пообщаемся?')

    def textMessage(bot, update):
        request = apiai.ApiAI('5787437579:AAGJFPuoLlpvTKoip7SiOytTrygj1qF4Xgo').text_request()  # Токен API к Dialogflow
        request.lang = 'ru'  # На каком языке будет послан запрос
        request.session_id = 'BatlabAIBot'  # ID Сессии диалога (нужно, чтобы потом учить бота)
        request.query = update.message.text  # Посылаем запрос к ИИ с сообщением от юзера
        responseJson = json.loads(request.getresponse().read().decode('utf-8'))
        response = responseJson['result']['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
        # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
        if response:
            bot.send_message(chat_id=update.message.chat_id, text=response)
        else:
            bot.send_message(chat_id=update.message.chat_id, text='Я Вас не совсем понял!')


    start_command_handler = CommandHandler('start', startCommand)
    text_message_handler = MessageHandler(Filters.text, textMessage)
    # Добавляем хендлеры в диспетчер
    dispatcher.add_handler(start_command_handler)
    dispatcher.add_handler(text_message_handler)

    bot.infinity_polling()
