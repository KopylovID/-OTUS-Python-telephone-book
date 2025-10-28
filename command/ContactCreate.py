import logging
from dataclasses import asdict

from command.Command import Command
from common.contact import Contact
from common.data import Data
from common.function import get_input, show

LOG = logging.getLogger(__name__)

class ContactCreate(Command):
    description = 'создать контакт'

    def __init__(self, data: Data):
        self.data: Data = data

    def get_params(self) -> Contact:
        contact = Contact()
        try:
            contact.name = get_input('Введите Имя: ')
            contact.phone = get_input('Введите Фелефон: ')
            contact.note = get_input('Введите Комментарий: ')
        except Exception as exc:
            show('Неизвестная ошибка при заведении полей! - просьба обратится в поддержку')
            LOG.exception(exc, exc_info=True)
        return contact

    def execute(self) -> None:
        LOG.debug(f'Запуск команды {self.description}')
        contact = self.get_params()
        if contact.is_active:
            show(f'Добавлен контакт ИД: {self.data.insert(asdict(contact))}')
        else:
            show('Контакт не содержит данных - добавление отменено!')