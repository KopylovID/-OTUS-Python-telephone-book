import json
import logging
from pathlib import Path

from command.Command import Command
from common.data import Data
from common.function import get_input, show

LOG = logging.getLogger(__name__)

class FileSave(Command):
    description = 'сохранить файл'

    def __init__(self, data: Data):
        self.data: Data = data

    def get_params(self) -> str:

        file_path = None

        try:
            __path = Path(get_input('Введите полный путь к файлу: '))
            if __path.name == '' or __path.name is None:
                __path = r'./temp/tb.json'
        except Exception as exc:
            show('Неизвестная ошибка! - просьба обратится в поддержку')
            LOG.exception(exc, exc_info=True)
        else:
            file_path = str(__path)

        return file_path

    def execute(self):
        LOG.debug(f'Запуск команды {self.description}')
        file_path = self.get_params()
        if file_path is not None:
            try:
                with open(file_path, 'w', encoding='utf-8') as file:
                    json.dump(self.data.data, file, ensure_ascii=False)
            except Exception as exc:
                show('Неизвестная ошибка при открытии файла! - просьба обратится в поддержку')
                LOG.exception(exc, exc_info=True)
