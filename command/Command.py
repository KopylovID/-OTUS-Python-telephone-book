from abc import ABC, abstractmethod


class Command(ABC):
    """Абстрактный класс команд"""

    description = None

    @property
    def description(self):
        """
        Описание команды
        :return: Строка с описанием команды
        """
        return self.description

    def get_params(self):
        """
        Получение параметров. Метод получения параметров для выполнения команды
        :return: Необходимо переопределение. Для каждой команды свой
        """
        raise NotImplementedError("Метод получения параметров не определен!")

    @abstractmethod
    def execute(self):
        """
        Исполнение. Метод выполнения команды
        :return: Необходимо переопределение. Для каждой команды свой
        """
        raise NotImplementedError("Команда не определена!")
