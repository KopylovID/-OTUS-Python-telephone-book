from abc import ABC
from common.function import show, get_input

class View(ABC):

    def show(self, data):
        show(data)

    def get_input(self, message: str = '') -> str:
        return get_input(message)




