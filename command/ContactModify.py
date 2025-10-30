import logging
from dataclasses import asdict
from typing import Tuple

from command.Command import Command
from common.contact import Contact
from common.data import Data
from common.function import get_input, show

LOG = logging.getLogger(__name__)

class ContactModify(Command):
    description = 'изменить контакт'

    def __init__(self, data: Data):
        self.data: Data = data

    def get_params(self) -> Tuple[str, Contact]:
        contact = Contact()
        try:
            id = str(get_input('Введите ИД изменяемого контакта: '))

            contact = Contact(**dict(self.data.data[id]))

            name = get_input(f'Введите Имя (нажмите Enter, чтобы оставить "{contact.name}" без изменения): ')
            phone = get_input(f'Введите Фелефон (нажмите Enter, чтобы оставить "{contact.phone}" без изменения): ')
            note = get_input(f'Введите Комментарий (нажмите Enter, чтобы оставить "{contact.note}" без изменения): ')

            if name != '': contact.name = name
            if phone != '': contact.phone = phone
            if note != '': contact.note = note

        except TypeError:
            show('ИД не является числом!')
            id = ''
        except KeyError:
            show('Не найден указанный контакт')
            id = ''
        except Exception as exc:
            show('Неизвестная ошибка при заведении полей! - просьба обратится в поддержку')
            id = ''
            LOG.exception(exc, exc_info=True)

        return id, contact

    def execute(self):
        LOG.debug(f'Запуск команды {self.description}')
        id, contact = self.get_params()
        if id != '':
            show(f'Обновлен контакт ИД: {self.data.update(str(id), asdict(contact))} - {contact.name}')

