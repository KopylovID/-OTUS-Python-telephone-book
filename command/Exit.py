from command.Command import Command


class Exit(Command):
    description = 'выход'

    def execute(self):
        from common.tb_exception import StopProcessing
        raise StopProcessing()