class Command:

    description = None

    @property
    def description(self):
        return self.description

    def execute(self):
        raise NotImplementedError('Команда не определена!')


class FileOpen(Command):
    description = 'открыть файл'


class FileSave(Command):
    description = 'сохранить файл'


class ContactShow(Command):
    description = 'показать все контакты'


class ContactCreate(Command):
    description = 'создать контакт'


class ContactFind(Command):
    description = 'найти контакт'


class ContactModify(Command):
    description = 'изменить контакт'


class ContactDelete(Command):
    description = 'удалить контакт'


class Exit(Command):
    description = 'выход'

    def execute(self):
        from tb_exception import StopProcessing
        raise StopProcessing()