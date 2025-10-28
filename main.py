import logging.config

logging.config.fileConfig('logging.conf')
LOG = logging.getLogger(__name__)

from telephone_book.telephone_book import TelephoneBook
from common.tb_exception import NoCommand, StopProcessing

from common.function import show

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
            tb.get_menu_input()

            LOG.debug('Выполняем комманду')
            tb.item_execute()
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