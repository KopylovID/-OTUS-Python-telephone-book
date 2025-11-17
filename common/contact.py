from dataclasses import dataclass


@dataclass
class Contact:
    """Класс данных - контакт"""

    name: str = ""
    phone: str = ""
    note: str = ""

    @property
    def is_active(self):
        """Проверка насколько полноценная информация для идентификации контакта"""

        return False if self.name == "" and self.phone == "" else True
