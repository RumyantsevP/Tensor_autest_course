# Напишите класс RomanNums
# Экземпляр класса создается из строки - Римского числа.
# Реализуйте методы класса:
# 1. from_roman, который переводит римскую запись числа в арабскую
# 2. is_palindrome, метод определяет, является ли арабское число палиндромом (True - является, иначе False)
# т.е. имеет ли одинаковое значение число при чтении слева направо и справа налево
# Например (Ввод --> Вывод) :
# RomanNums('MMMCCLXIII').from_roman() --> 3263
# RomanNums('CMXCIX').is_palindrome() --> True

# Здесь пишем код
class RomanNums:
        """
        Класс используется для:
        1. Перевод римского числа в арабское
        2. Проверка является ли полученное арабское число полиндромом
        """
        def __init__(self, roman_number):
                """
                Инициализация римского числа
                :param roman_number: римское число (в формате строки)
                """
                self.roman_number = roman_number
        def from_roman(self):
                """
                Перевод римского числа в арабское
                :return: арабское число
                """
                arab_number = 0  # Задаем арабское число равное "0"
                new_dict = {}  # Создаем пустой словарь, в котором "key" = римская цифра, "value" = аналогичное арабская цифра
                new_dict['M'] = 1000  # Римская цифра "M" соответствует арабской цифре "1000"
                new_dict['CM'] = 900  # Римская цифра "CM" соответствует арабской цифре "900"
                new_dict['D'] = 500  # Римская цифра "D" соответствует арабской цифре "500"
                new_dict['CD'] = 400  # Римская цифра "CD" соответствует арабской цифре "400"
                new_dict['C'] = 100  # Римская цифра "C" соответствует арабской цифре "100"
                new_dict['XC'] = 90  # Римская цифра "XC" соответствует арабской цифре "90"
                new_dict['L'] = 50  # Римская цифра "L" соответствует арабской цифре "50"
                new_dict['XL'] = 40  # Римская цифра "XL" соответствует арабской цифре "40"
                new_dict['X'] = 10  # Римская цифра "X" соответствует арабской цифре "10"
                new_dict['IX'] = 9  # Римская цифра "IX" соответствует арабской цифре "9"
                new_dict['V'] = 5  # Римская цифра "V" соответствует арабской цифре "5"
                new_dict['IV'] = 4  # Римская цифра "IV" соответствует арабской цифре "4"
                new_dict['I'] = 1  # Римская цифра "I" соответствует арабской цифре "1"
                for key, value in new_dict.items():  # Пробегаем по ключам (key) и значениям (value) в словаре
                    while self.roman_number.startswith(key):  # Пока строка начинается с символа соответствующего ключу "key"
                        arab_number += value  # Добавляем к арабскому числу значение, соответствующее ключу
                        self.roman_number = self.roman_number[len(key):]  # При помощи среза убираем из начала строки кол-во символов, равное длине ключа
                return arab_number  # Возвращаем значение арабского числа

        def is_palindrome(self):
                """
                Метод для проверки, является ли арабское число палиндромом
                :return: Является ли арабское число палиндромом (True) или НЕ является арабское число палиндромом (False)
                """
                palindrom_number = str(RomanNums.from_roman(self))  # Кладем в переменную значение арабского числа в формате строки.
                                                                    # Арабское число из римского получаем в функции "from_roman"
                if palindrom_number == palindrom_number[::-1]:  # Если полученная строка равна полученной перевернутой строке
                        return True  # Арабское число палиндром
                else:  # Иначе
                        return False  # Арабское число не палиндром

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [RomanNums('MMMCCLXIII').from_roman,
        RomanNums('CXXXIV').from_roman,
        RomanNums('LXXXVI').from_roman,
        RomanNums('MCDV').from_roman,
        RomanNums('CMLXXVIII').from_roman,
        RomanNums('MMMCDIV').from_roman,
        RomanNums('CMX').from_roman,
        RomanNums('MMCCCLXXXVIII').from_roman,
        RomanNums('MMVIII').from_roman,
        RomanNums('MCLXXIX').from_roman,
        RomanNums('MMMDCCXCV').from_roman,
        RomanNums('CMLXXXVIII').from_roman,
        RomanNums('CMXCIX').from_roman,
        RomanNums('CDXLIV').from_roman,
        RomanNums('CMXCIX').is_palindrome,
        RomanNums('CDXLIV').is_palindrome,
        RomanNums('MMMCCLXIII').is_palindrome,
        RomanNums('CXXXIV').is_palindrome,
        RomanNums('V').is_palindrome,
        RomanNums('MI').is_palindrome,
        RomanNums('XXX').is_palindrome,
        RomanNums('D').is_palindrome,
        ]


test_data = [3263, 134, 86, 1405, 978, 3404, 910, 2388, 2008, 1179, 3795, 988, 999, 444,
             True, True, False, False, True, True, False, False]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')