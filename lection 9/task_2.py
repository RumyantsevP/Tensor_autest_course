# Напишите декоратор func_log, который может принимать аргумент file_log (Путь до файла), по умолчнию равен 'log.txt'
# Декоратор должен дозаписывать в файл имя вызываемой функции (можно получить по атрибуту __name__), дату и время вызова
# по формату:
# имя_функции вызвана %d.%m %H:%M:%S
# Для вывода времени нужно использовать модуль datetime и метод .strftime()
# https://pythonworld.ru/moduli/modul-datetime.html
# https://docs.python.org/3/library/datetime.html
#
# Например
# @func_log()
# def func1():
#     time.sleep(3)
#
# @func_log(file_log='func2.txt')
# def func2():
#     time.sleep(5)
#
# func1()
# func2()
# func1()
#
# Получим:
# в log.txt текст:
# func1 вызвана 30.05 14:12:42
# func1 вызвана 30.05 14:12:50
# в func2.txt текст:
# func2 вызвана 30.05 14:12:47

# Со звёздочкой. ДЕЛАТЬ НЕ ОБЯЗАТЕЛЬНО.
# help(func1) должен выводит одинаковый текст, когда есть декоратор на функции func1 и когда его нет
# Реализовать без подключения новых модулей и сторонних библиотек.


import datetime

# Здесь пишем код
import datetime

def func_log(file_log='log.txt'):
    """ Декоратор с аргументом по умолчанию"""
    def my_decorator(func):
        def wrapper():
            func()
        return func
    return my_decorator

@func_log()  # Декоратор с принимаемым аргументом по умолчанию ("log.txt")
def func1():
    for_first_function = open(r'C:\Users\pn.rumyancev\Tensor_autotest_course\lection 9\test_file\log.txt', mode='a', encoding='utf-8')  # Файл в режиме добавления
    a = datetime.datetime.now()  # Получаем актуальные дата/время
    for_first_function.write(f'{func1.__name__} вызвана {a.strftime("%d.%m %H:%M:%S")}\n')  # Добавляем в файл имя функции и выводим дату/время в требуемом формате

@func_log(file_log='func2.txt')  # Декоратор с принимаемым аргументом "func2.txt"
def func2():
    for_second_function = open(r'C:\Users\pn.rumyancev\Tensor_autotest_course\lection 9\test_file\func2.txt', mode='a', encoding='utf-8')
    a = datetime.datetime.now()
    for_second_function.write(f'{func2.__name__} вызвана {a.strftime("%d.%m %H:%M:%S")}\n')

func1()
func2()
func1()