from loader import bot
from States.dialog_states import dialog_states
from config_data import config
from telebot.types import Message


@bot.message_handler(content_types=['text'], state=dialog_states.ask_about_mood)
def specify_mood(message: Message):
    if message.text.lower() in config.content_words["bad words"]:
        bot.send_message(chat_id=message.chat.id, text='Расскажи мне обо всем')
    elif message.text.lower() in config.content_words["good words"]:
        bot.send_message(chat_id=message.chat.id, text='Это замечательно!')