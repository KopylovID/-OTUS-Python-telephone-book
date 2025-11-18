from command.command import Command


class Exit(Command):
    """Команда: Выход из обработки"""

    description = 'выход'

    def execute(self):
        """
        Исполнение. Генерация исключения для выхода из программы
        :return: None
        """
        from common.tb_exception import StopProcessing
        raise StopProcessing()