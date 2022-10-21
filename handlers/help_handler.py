from loader import bot
from telebot.types import Message


@bot.message_handler(commands=['help'])
def show_help_info(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Доступные команды:\n'
                                                   '🔘/help - вывести список команд\n'
                                                   '🔘/start - запустить бота')