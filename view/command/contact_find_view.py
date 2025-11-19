import logging

from view.command.contact_show_view import ContactShowView

LOG = logging.getLogger(__name__)


class ContactFindView(ContactShowView):
    """Представление команды - Поиск контакта"""

    def error(self):
        self.show("Поиск не дал результатов!")

    def get_params(self):
        """
        Исполнение. Ввод параметров для поиска
        :return: None
        """

        name = self.get_input("Введите имя контакта для поиска: ")
        return name
