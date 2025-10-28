from abc import ABC, abstractmethod


class Command(ABC):
    description = None

    @property
    def description(self):
        return self.description

    def get_params(self):
        raise NotImplementedError('Метод получения параметров не определен!')

    @abstractmethod
    def execute(self):
        raise NotImplementedError('Команда не определена!')