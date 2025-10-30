import json
from typing import Dict


class Data:

    __data: Dict = dict()
    __data_seq: int = 0
    __action_id: int = 0

    @property
    def seq_values(self):
        return self.__data_seq

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data
        if self.__data:
            self.__data_seq = max(int(el) for el in self.__data)

    def __str__(self):
        return json.dumps(self.data, ensure_ascii=False)

    def update(self, idx: str, data: Dict) -> None:
        self.data[str(idx)] = data
        return idx

    def insert(self, data: Dict) -> int:
        self.__data_seq += 1
        self.data[self.__data_seq] = data
        return self.__data_seq

    def delete(self, idx: str) -> None:
        del self.data[idx]
        return idx

    def find(self) -> None:
        pass

    def set_action(self, ixd: int):
        if ixd in self.data:
            self.__action_id = ixd
