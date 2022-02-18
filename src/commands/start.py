from telegram import Update, ParseMode
from telegram.ext import CommandHandler, CallbackContext, Dispatcher

from commands.command import Command


class StartCommand(Command):
    def register(self, dispatcher: Dispatcher):
        dispatcher.add_handler(CommandHandler('start', self._command))

    def _command(self, update: Update, context: CallbackContext):
        text = f"Hello, I am {context.bot.name}\\!"
        context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode=ParseMode.MARKDOWN_V2)
