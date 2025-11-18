import logging
from pathlib import Path

from view.command.command_view import CommandView

LOG = logging.getLogger(__name__)


class FileOpenView(CommandView):
    """Представление команды - Открытие файла телефонного справочника"""

    def succes(self, file_path:str):
        """Успешная загрузка файла"""
        self.show(f"Файл {Path(file_path).name} успешно загружен")

    def error(self, message:str):
        """Ошибка при загрузке файла"""
        self.show(f"Ошибка при открытии файла! - просьба обратится в поддержку\n{message}")

    def get_params(self) -> str:
        """
        Получение параметров. Получение пути к требуемому файлу.
        :return: Строка. абсолютный путь к файлу
        """

        file_path = None

        try:
            default_path = r"./temp/tb.json"
            path = self.get_input(
                f"Введите полный путь к файлу (нажмите Enter для значения по умолчанию: {default_path}): "
            )

            if path is None or path == "":
                path = default_path
            path = Path(path)

            if not path.is_file():
                raise FileExistsError("Указанный путь не является файлом")
            elif not path.exists():
                raise FileNotFoundError("Файл по указанному пути не существует")

        except (FileExistsError, FileNotFoundError) as exc:
            self.show(str(exc))
            LOG.exception(exc, exc_info=True)
        except Exception as exc:
            self.show("Неизвестная ошибка! - просьба обратится в поддержку")
            LOG.exception(exc, exc_info=True)
        else:
            file_path = str(path)

        return file_path
