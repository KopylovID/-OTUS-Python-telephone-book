import logging
from dataclasses import asdict

from command.command import Command
from common.data import Data
from common.tb_exception import NoContactData
from view.command.contact_create_view import ContactCreateView

LOG = logging.getLogger(__name__)


class ContactCreate(Command):
    """Команда: Создание контакта"""

    description = "создать контакт"

    def __init__(self, data: Data, view: ContactCreateView):
        self.data: Data = data
        self.view: ContactCreateView = view

    def execute(self) -> None:
        """
        Исполнение. Создание контакта
        :return: None
        """
        LOG.debug(f"Запуск команды {self.description}")

        try:
            contact = self.view.get_params()
            if not contact.is_active:
                raise NoContactData()
            self.view.succes(self.data.insert(asdict(contact)))
        except Exception as exc:
            self.view.error(exc)
            LOG.exception(exc)
