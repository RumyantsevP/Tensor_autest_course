# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.smoke  # Маркируем тест как smoke-тест
def test_1():
    """
    Оба числа целые
    """
    assert all_division(6, 2) == 3

def test_new_2():
    """
    Делимое число является нулем
    """
    assert all_division(0, 5) == 0

@pytest.mark.smoke  # Маркируем тест как smoke-тест
def test_new_3():
    """
    Если один из элементов не число, то генерируется исключение 'TypeError'
    """
    with pytest.raises(TypeError):
        assert all_division('a', 9)

def test_4():
    """
    В результате деления получается отрицательное число
    """
    assert all_division(6, -2) == -3

def test_zero():
    """
    При попытке деления на ноль генерируется исключение 'ZeroDivisionError'
    """
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)