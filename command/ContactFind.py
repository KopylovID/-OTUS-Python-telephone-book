import logging
from typing import Dict

from command.Command import Command
from common.contact import Contact
from common.data import Data
from common.function import get_input, show

LOG = logging.getLogger(__name__)


class ContactFind(Command):
    """Команда: Поиск контакта"""

    description = "найти контакт"

    def __init__(self, data: Data):
        self.data: Data = data

    def execute(self):
        """
        Исполнение. Поиск контакта
        :return: None
        """

        LOG.debug(f"Запуск команды {self.description}")
        name = str(get_input("Введите имя контакта для поиска: "))
        data: Dict = dict()
        for id, contact in self.data.data.items():
            if str(contact["name"]).find(name) != -1:
                data[id] = contact

        if data:
            template = """id={id}, name={name}, phone={phone}, comment={comment}\n"""
            result = "Список контактов:\n"
            for key, value in data.items():
                result += template.format(
                    id=key, name=value.get("name"), phone=value.get("phone"), comment=value.get("note")
                )
            show(result.rstrip("\n"))
        else:
            show("Поиск не дал результатов!")
