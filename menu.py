from typing import List
from command import Command
from tb_exception import NoCommand

class Menu:

    def __init__(self, command_list:List[Command]):
        self.command_list: List[Command] = command_list

    def __str__(self):
        menu_template:str = '\nДоступные варианты меню:\n{menu_list}'
        return menu_template.format(menu_list='\n'.join([f'{idx} - {el.description}' for idx, el in enumerate(self.command_list, 1)]))

    def execute(self, ixd:int = 0, *args, **kwargs):
        if 1 <= ixd <= len(self.command_list):
            return self.command_list[ixd-1].execute(*args, **kwargs)
        else:
            raise NoCommand('Данный пункт меню отсутствует!')