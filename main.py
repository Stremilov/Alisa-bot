from art import tprint
from loader import bot
from loguru import logger
from utils.set_bot_commands import set_default_commands
import handlers


if __name__ == "__main__":
    tprint('bot', font='block', chr_ignore=True)
    logger.add('debug_file', format='{time} {level} {message}', level='DEBUG', rotation='6:00', compression='zip')
    set_default_commands(bot)
    bot.infinity_polling()
