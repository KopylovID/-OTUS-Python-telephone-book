import logging

from common.contact import Contact
from common.tb_exception import SkipProcessing
from common.function import get_input, show

LOG = logging.getLogger(__name__)
from view.command.command_view import CommandView

class ContactDeleteView(CommandView):
    """Представление команды - Удаление контакта"""


    def succes(self, id:str):
        """Успешная загрузка файла"""
        self.show(f"Удален контакт ИД: {id}")

    def get_contact_id(self) -> str:
        try:
            id = str(int(self.get_input("Введите ИД удаляемого контакта: ")))
        except (TypeError, ValueError):
            self.show("ИД не является числом!")
            raise SkipProcessing()
        return id

    def get_approve(self, id:str, contact: Contact) -> None:
        """
        Получение параметров. Получение ИД удаляемого контакта от пользователя
        :return: ИД контакта строка | ''
        """
        try:

            action = get_input(
                f'Вы действительно хотите удалить контакт {id}-"{contact.name}":({contact.phone})?; yes/no:'
            )

            if action != "yes":
                raise ValueError("Удаление отменено!")

        except TypeError:
            show("ИД не является числом!")
            raise SkipProcessing()
        except KeyError:
            show("Не найден указанный контакт")
            raise SkipProcessing()
        except ValueError as exc:
            show(str(exc))
            raise SkipProcessing()
