# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
a = '0123456789'  # Строка из символов, которые нужно удалить
in_old_file = open(r'C:\Users\pn.rumyancev\Tensor_autotest_course\lection 9\test_file\task1_data.txt', encoding='utf-8')  # В режиме чтения
in_new_file = open(r'C:\Users\pn.rumyancev\Tensor_autotest_course\lection 9\test_file\task1_answer.txt', mode='a', encoding='utf-8')  # В режиме добавления
list_row = in_old_file.readlines()  # Список из строк исходного текста из файла "task1_data.txt"
for i in list_row:
    new_str = ''
    for j in i:
        if j not in a:
            new_str += j
    in_new_file.write(new_str)  # Записываем измененный текст в файл "task1_answer.txt"


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
