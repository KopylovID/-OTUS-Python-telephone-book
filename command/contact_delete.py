import logging

from command.command import Command
from common.contact import Contact
from common.data import Data
from common.tb_exception import SkipProcessing
from view.command.contact_delete_view import ContactDeleteView

LOG = logging.getLogger(__name__)


class ContactDelete(Command):
    """Команда: Удаление контакта"""

    description = "удалить контакт"

    def __init__(self, data: Data, view: ContactDeleteView):
        self.data: Data = data
        self.view: ContactDeleteView = view
        self.contact_id: str = None


    def execute(self) -> None:
        """
        Исполнение. Удаление контакта
        :return: None
        """
        LOG.debug(f"Запуск команды {self.description}")
        try:
            self.contact_id = str(self.view.get_contact_id())
            contact = Contact(**dict(self.data.data[self.contact_id]))
            self.view.get_approve(self.contact_id, contact)
            self.data.delete(self.contact_id)
        except SkipProcessing:
            pass
        except Exception as exc:
            self.view.show("Неизвестная ошибка при заведении полей! - просьба обратится в поддержку")
            LOG.exception(exc, exc_info=True)
        else:
            self.view.succes(self.contact_id)
