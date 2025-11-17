import logging
from typing import List
from command.Command import Command
from common.tb_exception import NoCommand
from common.function import show

LOG = logging.getLogger(__name__)


class Menu:
    """Меню телефонного справочника"""

    def __init__(self, command_list: List[Command]):
        self.command_list: List[Command] = command_list

    def __str__(self):
        menu_template: str = "\nДоступные варианты меню:\n{menu_list}"
        return menu_template.format(
            menu_list="\n".join([f"{idx} - {el.description}" for idx, el in enumerate(self.command_list, 1)])
        )

    def get_input(self) -> int:
        """Предназначена для получения пункта меню от пользователя"""
        number = 0

        while number == 0:
            try:
                number = int(input("Введите номер пункта меню: "))
            except (TypeError, ValueError) as exc:
                show("Ожидалось числовое значение!")
                LOG.exception(exc, exc_info=True)
        return number

    def execute(self, ixd: int = 0):
        """Функция выполнения определенной команды"""
        if 1 <= ixd <= len(self.command_list):
            return self.command_list[ixd - 1].execute()
        else:
            raise NoCommand("Данный пункт меню отсутствует!")
