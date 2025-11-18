import logging

from command.command import Command
from common.contact import Contact
from common.data import Data
from common.function import get_input, show

LOG = logging.getLogger(__name__)


class ContactDelete(Command):
    """Команда: Удаление контакта"""

    description = "удалить контакт"

    def __init__(self, data: Data):
        self.data: Data = data

    def get_params(self) -> str:
        """
        Получение параметров. Получение ИД удаляемого контакта от пользователя
        :return: ИД контакта строка | ''
        """
        try:
            id = str(get_input("Введите ИД удаляемого контакта: "))

            contact = Contact(**dict(self.data.data[id]))

            action = get_input(
                f'Вы действительно хотите удалить контакт {id}-"{contact.name}":({contact.phone})?; yes/no:'
            )

            if action != "yes":
                raise ValueError("Удаление отменено!")

        except TypeError:
            show("ИД не является числом!")
            id = ""
        except KeyError:
            show("Не найден указанный контакт")
            id = ""
        except ValueError as exc:
            show(str(exc))
            id = ""
        except Exception as exc:
            show("Неизвестная ошибка при заведении полей! - просьба обратится в поддержку")
            id = ""
            LOG.exception(exc, exc_info=True)

        return id

    def execute(self) -> None:
        """
        Исполнение. Удаление контакта
        :return: None
        """
        LOG.debug(f"Запуск команды {self.description}")
        id = str(self.get_params())
        if id != "":
            show(f"Удален контакт ИД: {self.data.delete(id)}")
