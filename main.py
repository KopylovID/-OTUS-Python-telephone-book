import logging
import logging.config

logging.config.fileConfig('logging.conf')
LOG = logging.getLogger(__name__)

from telephone_book import TelephoneBook
from tb_exception import NoCommand, StopProcessing


def show(message:str):
    '''Предназначена для отображения сообщений пользователю'''
    print(message)


def get_input() -> int:
    '''Предназначена для получения пункта меню от пользователя'''
    number = 0

    while number == 0:
        try:
            number = int(input("Введите номер пункта меню: "))
        except TypeError:
            show('Ожидалось числовое значение!')
    return number


if __name__ == '__main__':
    LOG.debug('Запуск')

    LOG.debug('Создаем телефонный справочник')
    tb = TelephoneBook()

    while True:
        LOG.debug('Отображаем меню')
        show(tb.get_menu())

        LOG.debug('Обработка')
        try:
            LOG.debug('Получаем номер пункта меню')
            item = get_input()

            LOG.debug('Выполняем комманду')
            tb.item_execute(item)
        except NoCommand as exc:
            show(exc)
            continue
        except StopProcessing as exc:
            show(exc)
            break
        except NotImplementedError as exc:
            show(exc)
            continue
        except Exception as exc:
            LOG.exception(exc)
            raise

    LOG.debug('Завершение')