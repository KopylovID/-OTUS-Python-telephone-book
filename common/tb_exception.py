class NoCommand(Exception):
    """Исключенние для случая - когда нет подходящей команды для выполнения"""

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


class StopProcessing(Exception):
    """Исключение - взавершение обработки"""

    def __str__(self):
        return "Завершение обработки"
