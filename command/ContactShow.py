import logging
from typing import Dict

from command.Command import Command
from common.data import Data
from common.function import show

LOG = logging.getLogger(__name__)


class ContactShow(Command):
    description = 'показать все контакты'

    def __init__(self, data: Data):
        self.data: Data = data

    def execute(self) -> str:
        LOG.debug(f'Запуск команды {self.description}')
        data: Dict = dict(self.data.data)
        template = '''id={id}, name={name}, phone={phone}, comment={comment}\n'''
        result = 'Список контактов:\n'
        for key, value in data.items():
            result += template.format(
                id=key,
                name=value.get('name'),
                phone=value.get('phone'),
                comment=value.get('note')
            )
        show(result.rstrip('\n'))