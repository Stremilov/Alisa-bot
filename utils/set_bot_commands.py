from loader import bot
from telebot.types import BotCommand
from config_data.config import base_commands


def set_default_commands(bot):
    bot.set_my_commands(
        [BotCommand(*i) for i in base_commands]
    )
