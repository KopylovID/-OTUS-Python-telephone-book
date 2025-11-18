from abc import ABC, abstractmethod
import json


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

    @abstractmethod
    def execute(self, params: json = None):
        """
        Исполнение. Метод выполнения команды
        :return: Необходимо переопределение. Для каждой команды свой
        """
        raise NotImplementedError("Команда не определена!")
