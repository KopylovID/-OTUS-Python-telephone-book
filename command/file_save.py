import json
import logging
from pathlib import Path

from command.command import Command
from common.data import Data
from view.command.file_save_view import FileSaveView

LOG = logging.getLogger(__name__)


class FileSave(Command):
    """Команда: Сохранение файла телефонного справочника"""

    description = "сохранить файл"

    def __init__(self, data: Data, view: FileSaveView):
        self.data: Data = data
        self.view: FileSaveView = view

    def execute(self):
        """
        Исполнение. Сохранение файла по заданному пути
        :return: None
        """

        LOG.debug(f"Запуск команды {self.description}")
        file_path = self.view.get_params()
        if file_path is not None:
            try:
                with open(file_path, "w", encoding="utf-8") as file:
                    json.dump(self.data.data, file, ensure_ascii=False, indent=2)
            except Exception as exc:
                self.view.error(exc)
                LOG.exception(exc, exc_info=True)
            else:
                self.view.succes(file_path)
