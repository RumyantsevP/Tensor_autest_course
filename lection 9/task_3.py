# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open(r'C:\Users\pn.rumyancev\Tensor_autotest_course\lection 9\test_file\task_3.txt', encoding='utf-8') as shopping_file:
    shopping_strings = shopping_file.readlines()
    summa = 0
    buy_list = []
for i in shopping_strings:  # Пробегаем по строкам покупок
    if i == '\n':
        buy_list.append(summa)
        summa = 0
        continue
    else:
        summa += int(i)  # К сумме добавляем элемент списка, переведя элемент к целому числу
buy_list.append(summa)
buy_list = sorted(buy_list, reverse=True)  # Отсортировываем список по убыванию
three_most_expensive_purchases = buy_list[0] + buy_list[1] + buy_list[2]  # Суммируем первые 3 первые элемента списка


assert three_most_expensive_purchases == 202346
