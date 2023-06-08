import pytest
import datetime

@pytest.fixture  # Фикстура для всех тестов класса
def actual_time_for_class():
    start_time_of_class = datetime.datetime.now()
    print(f'\nВремя начала выполнения класса с тестами: {start_time_of_class}')
    yield
    end_time_of_class = datetime.datetime.now()
    print(f'\nВремя окончания выполнения класса с тестами: {end_time_of_class}')

@pytest.fixture  # Фикстура для конкретного теста
def actual_time_for_one_test():
    start_time_of_test = datetime.datetime.now()
    yield
    end_time_of_test = datetime.datetime.now()
    work_time = end_time_of_test - start_time_of_test
    return print(f'\n Время выполнения теста {work_time}')




