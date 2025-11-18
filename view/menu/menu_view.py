import logging
from typing import List
from view.view import View

LOG = logging.getLogger(__name__)


class MenuView(View):

    def get_menu_item(self):
        """Предназначена для получения пункта меню от пользователя"""
        number = 0

        while number == 0:
            try:
                number = int(input("Введите номер пункта меню: "))
            except (TypeError, ValueError) as exc:
                self.show("Ожидалось числовое значение!")
                LOG.exception(exc, exc_info=True)

        return number

    def show_menu(self, command_list: List[str]):
        menu_template: str = "\nДоступные варианты меню:\n{menu_list}"
        self.show(
            menu_template.format(menu_list="\n".join([f"{idx} - {el}" for idx, el in enumerate(command_list, 1)]))
        )