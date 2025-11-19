import logging
from dataclasses import asdict

from command.command import Command
from common.contact import Contact
from common.data import Data
from common.tb_exception import SkipProcessing
from view.command.contact_modify_view import ContactModifyView

LOG = logging.getLogger(__name__)


class ContactModify(Command):
    """Команда: Изменение контакта"""

    description = "изменить контакт"

    def __init__(self, data: Data, view: ContactModifyView):
        self.data: Data = data
        self.view: ContactModifyView = view
        self.contact_id: str = None

    def execute(self):
        """
        Исполнение. Изменение контакта
        :return: None
        """
        LOG.debug(f"Запуск команды {self.description}")

        try:
            self.contact_id = self.view.get_contact_id()
            contact = Contact(**dict(self.data.data[self.contact_id]))
            contact = self.view.get_params(contact)
            self.data.update(self.contact_id, asdict(contact))
        except KeyError:
            self.view.show("Не найден указанный контакт")
        except SkipProcessing:
            pass
        except Exception as exc:
            self.view.show("Неизвестная ошибка при заведении полей! - просьба обратится в поддержку")
            LOG.exception(exc, exc_info=True)
        else:
            self.view.succes(self.contact_id, contact)
