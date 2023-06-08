# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest

@pytest.mark.usefixtures("actual_time_for_class")  # Создаем пользовательскую фикструру для класса с тестами
class TestClass:
    """
    Класс с фикстурой time_start_end_log которая печатает время начала выполнения и окончания тестов
    """

    def all_division(*arg1):
        division = arg1[1]
        for i in arg1[2:]:
             division /= i
        return division

    def test_1(self):
        assert self.all_division(6, 2) == 3

    def test_new_2(self):
        """
        Делимое число является нулем
        """
        assert self.all_division(0, 5) == 0

    def test_new_3(self):
        """
        Если один из элементов не число, то генерируется исключение 'TypeError'
        """
        with pytest.raises(TypeError):
            assert self.all_division('a', 9)

    def test_4(self):
        """
        В результате деления получается отрицательное число
        """
        assert self.all_division(6, -2) == -3

    def test_zero(self):
        """
        При попытке деления на ноль генерируется исключение 'ZeroDivisionError'
        """
        with pytest.raises(ZeroDivisionError):
            self.all_division(10, 0)

    def test_2(self, actual_time_for_one_test):  # Тест с фикстурой для конкретного теста
        """
        Тест с фикстурой "actual_time_for_one_test", высчитывающей время выполнения конкретного теста
        """
        summa = 0
        for i in range(1, 100000):  # Суммируем числа от одного с шагом 1
            summa += i