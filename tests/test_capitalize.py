# Нажмите кнопку Run чтобы запустить тесты.

# Файлы с исходным кодом можно посмотреть на вкладке "Files":
# src/capitalize.py        - тестируемая функция
# tests/test_capitalize.py - тесты функции

# Попробуйте изменять код функции/тестов, запуская проверки заново.

from capitalize import capitalize

assert capitalize('hello') == 'hello':
    raise Exception('Функция работает неверно!')

assert capitalize('') == '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
