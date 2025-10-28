from dataclasses import dataclass


@dataclass
class Contact:
    name:str = ''
    phone:str = ''
    note:str = ''

    @property
    def is_active(self):
        return False if self.name == '' and self.phone == '' else True