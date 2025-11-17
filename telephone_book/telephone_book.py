import logging

from command import *
from common.data import Data
from telephone_book.telephone_book_view import TelephoneBookView
from common.tb_exception import NoCommand, StopProcessing
from menu.menu import Menu

LOG = logging.getLogger(__name__)


class TelephoneBook:
    """Телефонный справочник"""

    __version: str = "0.0.0"

    def __init__(self):
        LOG.debug(f"Телефонный справочник - Версия {self.__version}")

        self.data = Data()               # Модель
        self.view = TelephoneBookView()  # Представление

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
            ]
        )
        self.menu_index = 1

    def get_menu_input(self) -> None:
        """Функция получения выбранного пункта меню"""
        self.menu_index = self.view.get_menu_input()

    def item_execute(self):
        """Функция выполнения команды"""
        self.menu.execute(self.menu_index)

    def run(self):
        """Метод запуска телефонного справочника"""

        while True:
            LOG.debug("Отображаем меню")
            self.view.show_menu(self.menu.get_menu())

            LOG.debug("Обработка")
            try:
                LOG.debug("Получаем номер пункта меню и сохраняем индекс команды")
                self.get_menu_input()

                LOG.debug("Выполняем команду по индексу")
                self.item_execute()
            except NoCommand as exc:
                self.view.show(exc)
                continue
            except StopProcessing as exc:
                self.view.show(exc)
                break
            except NotImplementedError as exc:
                self.view.show(exc)
                continue
            except Exception as exc:
                LOG.exception(exc)
                raise
