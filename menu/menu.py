import logging
from typing import List
from command.command import Command
from view.menu.menu_view import MenuView
from common.tb_exception import NoCommand, StopProcessing

LOG = logging.getLogger(__name__)


class Menu:
    """Меню телефонного справочника"""

    def __init__(self, command_list: List[Command], menu_view: MenuView):
        self.command_list: List[Command] = command_list
        self.menu_view = menu_view
        self.menu_index = 1

    def get_menu(self) -> List[str]:
        return [el.description for el in self.command_list]

    def execute(self, ixd: int = 0):
        """Функция выполнения определенной команды"""
        if 1 <= ixd <= len(self.command_list):
            return self.command_list[ixd - 1].execute()
        else:
            raise NoCommand("Данный пункт меню отсутствует!")

    def run(self):

        while True:
            LOG.debug("Отображаем меню")
            self.menu_view.show_menu(self.get_menu())

            try:
                LOG.debug("Выбираенм пункт меню и сохраняем индекс команды")
                self.menu_index = self.menu_view.get_menu_item()

                LOG.debug("Выполняем команду по индексу")
                self.execute(self.menu_index)
            except NoCommand as exc:
                self.menu_view.show(exc)
                continue
            except StopProcessing as exc:
                self.menu_view.show(exc)
                break
            except NotImplementedError as exc:
                self.menu_view.show(exc)
                continue
            except Exception as exc:
                LOG.exception(exc)
                raise