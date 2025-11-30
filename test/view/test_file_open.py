import pytest
import logging
from contextlib import nullcontext as does_not_raise

log = logging.getLogger()
log.addHandler(logging.StreamHandler())

from view.command.file_open_view import FileOpenView

@pytest.mark.debug
@pytest.mark.parametrize("file_path,expectation", [
    pytest.param('./test/temp/tb_test.json', does_not_raise(), id="Корректный файл"),
    pytest.param('./test/temp/no_file.json', pytest.raises(FileExistsError), marks=pytest.mark.xfail, id="Не корректный файл")
])
def test_get_params(mocker, file_path: str, expectation: str):
    file_open_view = FileOpenView()

    test_get_input = mocker.patch('view.command.file_open_view.FileOpenView.get_input')
    test_get_input.return_value = rf'{file_path}'

    test_show = mocker.patch('view.command.file_open_view.FileOpenView.show')
    test_show.return_value = ''

    assert file_open_view.get_params() is not None
