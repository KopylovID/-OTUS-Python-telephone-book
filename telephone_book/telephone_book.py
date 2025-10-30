import logging

from command import *
from common.data import Data
from menu.menu import Menu

LOG = logging.getLogger(__name__)

class TelephoneBook:

    __version: str = '0.0.0'

    def __init__(self):
        LOG.debug(f'Телефонный справочник - Версия {self.__version}')
        self.data = Data()

        self.menu:Menu = Menu([
            FileOpen(self.data),
            FileSave(self.data),
            ContactShow(self.data),
            ContactCreate(self.data),
            ContactFind(self.data),
            ContactModify(self.data),
            ContactDelete(self.data),
            Exit()
        ])
        self.menu_index = 1

    def get_menu(self) -> str:
        return str(self.menu)

    def get_menu_input(self) -> None:
        self.menu_index = self.menu.get_input()

    def item_execute(self):
        self.menu.execute(self.menu_index)


