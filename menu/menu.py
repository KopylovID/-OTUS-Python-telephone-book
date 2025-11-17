import logging
from typing import List
from command.Command import Command
from common.tb_exception import NoCommand

LOG = logging.getLogger(__name__)


class Menu:
    """Меню телефонного справочника"""

    def __init__(self, command_list: List[Command]):
        self.command_list: List[Command] = command_list

    def get_menu(self) -> List[str]:
        return [el.description for el in self.command_list]

    def execute(self, ixd: int = 0):
        """Функция выполнения определенной команды"""
        if 1 <= ixd <= len(self.command_list):
            return self.command_list[ixd - 1].execute()
        else:
            raise NoCommand("Данный пункт меню отсутствует!")
