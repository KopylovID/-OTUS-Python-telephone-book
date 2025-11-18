import logging
from typing import Dict

from view.command.command_view import CommandView

LOG = logging.getLogger(__name__)


class ContactShowView(CommandView):
    """Представление команды - Отображение всех контактов"""

    def contact_show(self, data: Dict) -> None:
        """
        Отображение контактов
        :param data: Данные для отображения в формате словаря Data
        :return: None
        """

        template = """id={id}, name={name}, phone={phone}, comment={comment}\n"""
        result = "Список контактов:\n"
        for key, value in data.items():
            result += template.format(
                id=key, name=value.get("name"), phone=value.get("phone"), comment=value.get("note")
            )
        self.show(result.rstrip("\n"))
