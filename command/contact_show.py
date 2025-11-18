import logging
from typing import Dict

from command.command import Command
from common.data import Data
from view.command.contact_show_view import ContactShowView

LOG = logging.getLogger(__name__)


class ContactShow(Command):
    """Команда: Отображение всех контактов"""

    description = "показать все контакты"

    def __init__(self, data: Data, view: ContactShowView):
        self.data: Data = data
        self.view:ContactShowView = view

    def execute(self) -> str:
        """
        Исполнение. Отображение контактов
        :return: None
        """

        LOG.debug(f"Запуск команды {self.description}")
        data: Dict = dict(self.data.data)
        self.view.contact_show(data)