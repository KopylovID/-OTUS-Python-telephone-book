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

        from view.command.file_open_view import FileOpenView
        from view.command.file_save_view import FileSaveView
        from view.command.contact_show_view import ContactShowView
        from view.command.contact_create_view import ContactCreateView
        from view.command.contact_find_view import ContactFindView
        from view.command.contact_modify_view import ContactModifyView

        self.menu: Menu = Menu(
            [
                FileOpen(self.data, FileOpenView()),
                FileSave(self.data, FileSaveView()),
                ContactShow(self.data, ContactShowView()),
                ContactCreate(self.data, ContactCreateView()),
                ContactFind(self.data, ContactFindView()),
                ContactModify(self.data, ContactModifyView()),
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
