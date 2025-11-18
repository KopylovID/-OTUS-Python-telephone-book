import json
import logging
from pathlib import Path

from command.command import Command
from common.data import Data
from common.function import get_input, show

LOG = logging.getLogger(__name__)


class FileOpen(Command):
    """Команда: Открытие файла телефонного справочника"""

    description = "открыть файл"

    def __init__(self, data: Data):
        self.data: Data = data

    def get_params(self) -> str:
        """
        Получение параметров. Получение пути к требуемому файлу.
        :return: Строка. абсолютный путь к файлу
        """

        file_path = None

        try:
            default_path = r"./temp/tb.json"
            path = get_input(f"Введите полный путь к файлу (нажмите Enter для значения по умолчанию: {default_path}): ")

            if path is None or path == "":
                path = default_path
            path = Path(path)

            if not path.is_file():
                raise FileExistsError("Указанный путь не является файлом")
            elif not path.exists():
                raise FileNotFoundError("Файл по указанному пути не существует")

        except (FileExistsError, FileNotFoundError) as exc:
            show(str(exc))
            LOG.exception(exc, exc_info=True)
        except Exception as exc:
            show("Неизвестная ошибка! - просьба обратится в поддержку")
            LOG.exception(exc, exc_info=True)
        else:
            file_path = str(path)

        return file_path

    def execute(self) -> None:
        """
        Исполнение. Чтение файла по заданному пути
        :return: None
        """

        LOG.debug(f"Запуск команды {self.description}")
        file_path = self.get_params()
        if file_path is not None:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.data.data = json.load(file)
            except Exception as exc:
                show("Неизвестная ошибка при открытии файла! - просьба обратится в поддержку")
                LOG.exception(exc, exc_info=True)
            else:
                show(f"Файл {Path(file_path).name} успешно загружен")
