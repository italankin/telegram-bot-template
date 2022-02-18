import abc

from telegram.ext import Dispatcher


class Command:
    @abc.abstractmethod
    def register(self, dispatcher: Dispatcher):
        pass
