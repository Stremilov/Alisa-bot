from loader import bot
from States.dialog_states import dialog_states


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, text='Привет, сладкий! 😘'.format(message.from_user.username))
    bot.send_message(message.chat.id, text='Как твои дела?')
    bot.set_state(message.chat.id, dialog_states.ask_about_mood)
