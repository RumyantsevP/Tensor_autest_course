# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


# Здесь пишем код

letters = 'abcdefghijklmnopqrstuvwxyz'  # Строка с алтинскими буквами
def generate_random_name():
    """
    Генерирует два слова из латинских букв от 1 до 15 символов
    :return: Два сгенерированных слова
    """
    while True:  # Делаем цикл без указания конкретного кол-ва дальнейших вызовов функции
        number_1 = random.randrange(1, 16)  # Генерируем случайное число от 1 до 15 включительно
        number_2 = random.randrange(1, 16)
        new_string = ''.join(random.choice(letters) for i in range(0, number_1)) + ' ' + ''.join(random.choice(letters) for i in range(0, number_2))
        #  Собираем строку из латинских букв строки "letters" в количестве, сгенерированном в переменных number_1 и number_2,
        #  разделяя слова между собой пробелом
        yield new_string  # Возвращаем строку

gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
