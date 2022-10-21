from telebot.handler_backends import State, StatesGroup


class dialog_states(StatesGroup):
    say_hello = State()
    ask_about_mood = State()
