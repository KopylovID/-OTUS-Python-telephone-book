import json
from typing import Dict


class Data:

    __data: Dict = dict()
    __data_seq: int = 0

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def __str__(self):
        return json.dumps(self.data, ensure_ascii=False)

    def update(self) -> None:
        pass

    def insert(self, data: Dict) -> int:
        self.__data_seq += 1
        self.data[self.__data_seq] = data
        return self.__data_seq

    def delete(self) -> None:
        pass

    def find(self) -> None:
        pass

