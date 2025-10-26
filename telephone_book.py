import logging
from menu import Menu
from command import FileOpen, FileSave, ContactShow, ContactCreate, ContactFind, ContactModify, ContactDelete, Exit

LOG = logging.getLogger(__name__)

class TelephoneBook:

    __version: str = '0.0.0'

    def __init__(self):
        LOG.debug(f'Телефонный справочник - Версия {self.__version}')
        self.menu:Menu = Menu([FileOpen(), FileSave(), ContactShow(), ContactCreate(), ContactFind(), ContactModify(), ContactDelete(), Exit()])

    def get_menu(self) -> str:
        return str(self.menu)

    def item_execute(self, item:int, *args, **kwargs):
        self.menu.execute(item, *args, **kwargs)


