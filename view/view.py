from abc import ABC
from common.function import show

class View(ABC):

    def show(self, data):
        show(data)

