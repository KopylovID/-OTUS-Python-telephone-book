import json
from typing import Dict


class Data:
    """Класс для работы с данными телефонного справочника"""

    def __init__(self):
        self.__data: Dict = dict()
        self.__data_seq: int = 0
        self.__action_id: int = 0

    @property
    def seq_values(self):
        """Функция возвращающая текущий ИД последовательности"""
        return self.__data_seq

    @property
    def data(self):
        """Функция возвращающая полностью все данные справочника"""
        return self.__data

    @data.setter
    def data(self, data):
        """Функция сохраняющая данные справочника в паммять"""
        self.__data = data
        if self.__data:
            self.__data_seq = max(int(el) for el in self.__data)

    def __str__(self):
        return json.dumps(self.data, ensure_ascii=False)

    def update(self, idx: str, data: Dict) -> None:
        """Функция обновления данных по конкретному контакту"""
        self.data[str(idx)] = data
        return idx

    def insert(self, data: Dict) -> int:
        """Функция добавляющая новый контакт"""
        self.__data_seq += 1
        self.data[self.__data_seq] = data
        return self.__data_seq

    def delete(self, idx: str) -> None:
        """Функция удаления контакта"""
        del self.data[idx]
        return idx

    def find(self, attr_name:str, find_str:str) -> Dict:
        """Функция поиска определенного контакта"""
        result_data: Dict = dict()
        for id, entity in self.data.items():
            if str(entity.get(attr_name, '')).find(find_str) != -1:
                result_data[id] = entity
        return result_data

    def set_action(self, ixd: int):
        """Функция устанавливающая идентификатор текущего выбранного контакта"""
        if ixd in self.data:
            self.__action_id = ixd
