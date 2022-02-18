from telegram.ext import Updater

from config import Config
import commands


class Bot:
    def __init__(self, config: Config):
        self._updater = Updater(token=config.bot_token)
        self._dispatcher = self._updater.dispatcher
        self._commands = [
            commands.start.StartCommand(),
            commands.error_handler.ErrorCommand(config.admin_id)
        ]

    def run(self):
        pass
