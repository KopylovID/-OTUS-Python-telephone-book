import logging

from common.contact import Contact
from view.command.command_view import CommandView

LOG = logging.getLogger(__name__)


class ContactCreateView(CommandView):
    """Представление команды - Создание контакта"""

    def succes(self, contact_id: str):
        """Успешное добавление контакта"""
        self.show(f"Добавлен контакт ИД: {contact_id}")

    def error(self, message: str):
        """Ошибка при добавлении контакта"""
        self.show(message)

    def get_params(self) -> Contact:
        """
        Получение параметров. Получение параметров контакта от пользователя
        :return: Contact()
        """
        contact = Contact()
        try:
            contact.name = self.get_input("Введите Имя: ")
            contact.phone = self.get_input("Введите Фелефон: ")
            contact.note = self.get_input("Введите Комментарий: ")
        except Exception as exc:
            self.show("Неизвестная ошибка при заведении полей! - просьба обратится в поддержку")
            LOG.exception(exc, exc_info=True)
        return contact
