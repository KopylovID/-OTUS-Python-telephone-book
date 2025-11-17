import logging.config

logging.config.fileConfig('logging.conf')
LOG = logging.getLogger(__name__)

from telephone_book.telephone_book import TelephoneBook


if __name__ == '__main__':
    LOG.debug('Запуск')

    LOG.debug('Создаем телефонный справочник')
    tb = TelephoneBook()
    tb.run()

    LOG.debug('Завершение')