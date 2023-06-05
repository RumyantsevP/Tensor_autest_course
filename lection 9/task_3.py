# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
f = list(open(r'C:\Users\pn.rumyancev\Tensor_autotest_course\lection 9\test_file\task_3.txt', encoding='utf-8'))  # Кладем содержимое файла в переменную f в формате списка
summa = 0
a = []
for i in f:  # Пробегаем по элементам списка
    if i == '\n':
        a.append(summa)
        summa = 0
        continue
    else:
        summa += int(i)  # К сумме добавляем элемент списка, переведя элемент к целому числу
a.append(summa)
a = sorted(a, reverse=True)  # Отсортировываем список по убыванию
three_most_expensive_purchases = a[0] + a[1] + a[2]  # Суммируем первые 3 первые элемента списка


assert three_most_expensive_purchases == 202346
