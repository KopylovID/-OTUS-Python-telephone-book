from typing import Dict

from command.Command import Command
from common.data import Data
from common.function import show


class ContactShow(Command):
    description = 'показать все контакты'

    def __init__(self, data: Data):
        self.data: Data = data

    def execute(self) -> str:
        data: Dict = dict(self.data.data)
        template = '''id={id}, name={name}, phone={phone}, comment={comment}\n'''
        result = 'Список контактов:\n'
        for key, value in data.items():
            result += template.format(
                id=key,
                name=value.get('name'),
                phone=value.get('phone'),
                comment=value.get('comment')
            )
        show(result.rstrip('\n'))