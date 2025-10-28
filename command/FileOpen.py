import json
import os
from pathlib import Path

from command.Command import Command
from common.data import Data
from common.function import get_input, show


class FileOpen(Command):

    description = 'открыть файл'

    def __init__(self, data: Data):
        self.data: Data = data

    def get_params(self) -> str:

        file_path = None

        try:
            __path = Path(get_input('Введите полный путь к файлу: '))
            if not file_path.is_file():
                raise FileExistsError('Указанный путь не является файлом')
            elif not file_path.exists():
                raise FileNotFoundError('Файл по указанному пути не существует')
        except (FileExistsError, FileNotFoundError) as exc:
            show(str(exc))
        except Exception:
            show('Неизвестная ошибка! - просьба обратится в поддержку')
        else:
            file_path = str(__path)

        return file_path

    def execute(self) -> None :
        file_path = self.get_params()
        if file_path is not None:
            try:
                with os.open(file_path, mode='r', encoding='utf-8') as file:
                    self.data = json.load(file)
            except Exception:
                show('Неизвестная ошибка при открытии файла! - просьба обратится в поддержку')