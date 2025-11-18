from view.view import View
from abc import abstractmethod

class CommandView(View):
    """Абстрактный класс отображенгия команды"""

    @abstractmethod
    def get_params(self):
        """
        Получение параметров. Метод получения параметров для выполнения команды
        :return: Необходимо переопределение. Для каждой команды свой
        """
        raise NotImplementedError("Метод получения параметров не определен!")
