import pytest

from common.contact import Contact
from dataclasses import asdict
from typing import Tuple
from common.data import Data
from test.test_dataset import test_ds


class TestData:

    @pytest.mark.model
    @pytest.mark.parametrize("test_contact", test_ds)
    def test_insert(self, data_empty: Data, test_contact: Tuple[str, str, str]):
        data = data_empty
        contact = Contact(*test_contact)

        contact_id = data.insert(asdict(contact))
        assert len(data.data) > 0, "Отсутствуют записи!"
        assert Contact(**data.data[contact_id]) == contact, "Созданная запись не равна эталонной!"

    @pytest.mark.model
    def test_update(self, data_filled: Data):
        from random import choice

        data = data_filled
        contact = Contact()
        contact_id = str(choice(list(data.data.keys())))
        data.update(contact_id, asdict(contact))
        assert Contact(**data.data[contact_id]) == contact, "Обновленная запись не равна эталонной!"

    @pytest.mark.model
    def test_delete(self, data_filled: Data):
        from random import choice

        data = data_filled
        contact_amount_before = len(data.data)
        contact_id = choice(list(data.data.keys()))
        data.delete(contact_id)
        contact_amount_after = len(data.data)
        assert contact_amount_before - contact_amount_after == 1, "Количество записей не изменилось!"
        assert data.data.get(contact_id) is None, "Запись не была удалена!"
