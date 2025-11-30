import logging
from typing import Dict

from command.command import Command
from common.data import Data
from view.command.contact_find_view import ContactFindView

LOG = logging.getLogger(__name__)


class ContactFind(Command):
    """Команда: Поиск контакта"""

    description = "найти контакт"

    def __init__(self, data: Data, view: ContactFindView):
        self.data: Data = data
        self.view: ContactFindView = view

    def execute(self):
        """
        Исполнение. Поиск контакта
        :return: None
        """

        LOG.debug(f"Запуск команды {self.description}")

        name = self.view.get_params()
        data: Dict = self.data.find("name", name)

        if data:
            self.view.contact_show(data)
        else:
            self.view.error()
