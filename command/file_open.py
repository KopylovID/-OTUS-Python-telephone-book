import json
import logging

from command.command import Command
from common.data import Data
from view.command.file_open_view import FileOpenView


LOG = logging.getLogger(__name__)


class FileOpen(Command):
    """Команда: Открытие файла телефонного справочника"""

    description = "открыть файл"

    def __init__(self, data: Data, view: FileOpenView):
        self.data: Data = data
        self.view: FileOpenView = view

    def execute(self) -> None:
        """
        Исполнение. Чтение файла по заданному пути
        :return: None
        """

        LOG.debug(f"Запуск команды {self.description}")
        file_path = self.view.get_params()
        if file_path is not None:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    self.data.data = json.load(file)
            except Exception as exc:
                self.view.error(exc)
                LOG.exception(exc, exc_info=True)
            else:
                self.view.succes(file_path)
