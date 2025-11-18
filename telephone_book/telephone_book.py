import logging

from command import *
from common.data import Data
from view.telephone_book_view import TelephoneBookView

LOG = logging.getLogger(__name__)


class TelephoneBook:
    """Телефонный справочник"""

    __version: str = "0.0.0"

    def __init__(self):
        LOG.debug(f"Телефонный справочник - Версия {self.__version}")

        self.data = Data()  # Модель

        # region Menu
        from menu.menu import Menu
        from view.menu.menu_view import MenuView

        self.menu: Menu = Menu(
            [
                FileOpen(self.data),
                FileSave(self.data),
                ContactShow(self.data),
                ContactCreate(self.data),
                ContactFind(self.data),
                ContactModify(self.data),
                ContactDelete(self.data),
                Exit(),
            ],
            MenuView(),
        )
        # endregion

        self.view = TelephoneBookView()

    def run(self):
        """Метод запуска компонентов телефонного справочника"""
        try:
            self.menu.run()
        except KeyboardInterrupt:
            self.view.show("\nЗавершение программы")
