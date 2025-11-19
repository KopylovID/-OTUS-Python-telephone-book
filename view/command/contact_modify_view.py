import logging

from common.contact import Contact
from common.tb_exception import SkipProcessing
from view.command.command_view import CommandView

LOG = logging.getLogger(__name__)


class ContactModifyView(CommandView):
    """Представление команды - Изменение контакта"""

    def succes(self, id: str, contact: Contact):
        """Успешная загрузка файла"""
        self.show(f"Обновлен контакт ИД: {id} - {contact.name}")

    def error(self, message: str):
        """Ошибка при загрузке файла"""
        self.show(f"Ошибка при открытии файла! - просьба обратится в поддержку\n{message}")

    def get_contact_id(self) -> str:
        try:
            id = str(int(self.get_input("Введите ИД изменяемого контакта: ")))
        except (TypeError, ValueError):
            self.show("ИД не является числом!")
            raise SkipProcessing()
        return id

    def get_params(self, contact: Contact) -> Contact:
        """
        Получение параметров. Получение ИД контакта по которому требуется внести изменение
        :return: Contact()
        """

        try:

            name = self.get_input(f'Введите Имя (нажмите Enter, чтобы оставить "{contact.name}" без изменения): ')
            phone = self.get_input(f'Введите Фелефон (нажмите Enter, чтобы оставить "{contact.phone}" без изменения): ')
            note = self.get_input(
                f'Введите Комментарий (нажмите Enter, чтобы оставить "{contact.note}" без изменения): '
            )

            if name != "":
                contact.name = name
            if phone != "":
                contact.phone = phone
            if note != "":
                contact.note = note

        except Exception as exc:
            self.show("Неизвестная ошибка при заведении полей! - просьба обратится в поддержку")
            LOG.exception(exc, exc_info=True)
            raise SkipProcessing()

        return contact
