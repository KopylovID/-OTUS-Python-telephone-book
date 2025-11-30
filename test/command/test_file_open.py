import pytest
from contextlib import nullcontext as does_not_raise

from command import FileOpen
from common.data import Data

@pytest.mark.controller
@pytest.mark.parametrize("file_path,expectation", [
    pytest.param('./test/temp/tb_test_1.json', does_not_raise(), id="Корректный файл №1 - Распарсенный JSON"),
    pytest.param('./test/temp/tb_test_2.json', does_not_raise(), id="Корректный файл №2 - Строковый JSON"),
    pytest.param('./test/temp/tb_test_3.json', pytest.raises(Exception), marks=pytest.mark.xfail, id="Не корректный формат файла"),
    pytest.param('./test/temp/no_file.json', pytest.raises(FileNotFoundError), marks=pytest.mark.xfail, id="Не существующий файл")
])
def test_execute(mocker, data_empty: Data, file_path: str, expectation: str):
    data = data_empty
    file_open_view = mocker.patch("view.command.file_open_view.FileOpenView", autospec=True)
    file_open_view_obj = file_open_view.return_value
    file_open_view_obj.succes.return_value = 'OK'
    file_open_view_obj.error.return_value = 'ERROR'
    file_open_view_obj.get_params.return_value = rf'{file_path}'

    file_open = FileOpen(data, file_open_view_obj)
    file_open.execute()
    assert file_open.data.data is not None
