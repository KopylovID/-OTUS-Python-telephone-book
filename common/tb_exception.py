class NoCommand(Exception):
    """Исключенние для случая - когда нет подходящей команды для выполнения"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class StopProcessing(Exception):
    """Исключение - завершение обработки"""

    def __str__(self):
        return "Завершение обработки"


class NoContactData(Exception):
    """Исключение когда у контакта не заполнены поля"""

    def __str__(self):
        return "Контакт не содержит данных"

class SkipProcessing(Exception):
    """Исключение для пропуска обработки"""
    pass