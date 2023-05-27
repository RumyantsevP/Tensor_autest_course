# Напишите класс Segment
# Для его инициализации нужно два кортежа с координатами точек (x1, y1), (x2, y2)
# Реализуйте методы классы:
# 1. length, который возвращает длину нашего отрезка, с округлением до 2 знаков после запятой
# 2. x_axis_intersection, который возвращает True, если отрезок пересекает ось абцисс, иначе False
# 3. y_axis_intersection, который возвращает True, если отрезок пересекает ось ординат, иначе False
# Например (Ввод --> Вывод) :
# Segment((2, 3), (4, 5)).length() --> 2.83
# Segment((-2, -3), (4, 5)).x_axis_intersection() --> True
# Segment((-2, -3), (4, -5)).y_axis_intersection() --> False

# Здесь пишем код
class Segment:
    """
    Класс используется для:
    1. Определения длины отрезка по координатам двух точек
    2. Определяет пересекает ли отрезок ось абсцисс
    3. Определяет пересекает ли отрезок ось ординат
    """
    def __init__(self, point_1, point_2):
        """
        Инициализируем координаты для двух точек отрезка
        :param point_1: координаты первой точки
        :param point_2: координаты второй точки
        """
        self.point_1 = point_1
        self.point_2 = point_2

    def length(self) :
        """
        Метод для определения длины отрезка по координатам двух точек
        :return: длина отрезка, округленная до 2х знаков после запятой
        """
        length = ((self.point_2[0] - self.point_1[0]) ** 2 + (self.point_2[1] - self.point_1[1]) ** 2) ** 0.5
        # Вычислаем длину отрезка по стандартной формуле
        return round(length, 2)  # Возвращаем длину отрезка, округленную до 2х знаков после запятой

    def x_axis_intersection(self):
        """
        Метод для опредения пересекается ли отрезок с осью абсцисс
        :return: True - если пересекает, False - если не пересекает
        """
        if self.point_1[1] >= 0 and self.point_2[1] <= 0 or self.point_1[1] <= 0 and self.point_2[1] >= 0:
            # Если координата "Y" одной точки находятся ВЫШЕ либо на оси абсцисси, а координата "Y" другой точки НИЖЕ либо на оси абсцисс
            x_axis_intersection = True  # Отрезок пересекает ось абсцисс (возвращает True)
        else:  # Иначе
            x_axis_intersection = False  # Отрезок НЕ пересекает ось абсцисс (возвращает False)
        return x_axis_intersection  # Возвращаем информацию о том, преесекает ли отрезок ось абсцисс

    def y_axis_intersection(self):
        """
        Метод для опредения пересекается ли отрезок с осью ординат
        :return: True - если пересекает, False - если не пересекает
        """
        if self.point_1[0] >= 0 and self.point_2[0] <= 0 or self.point_1[0] <= 0 and self.point_2[0] >= 0:
            # Если координата "X" одной точки находятся ВЫШЕ либо на оси ординат, а координата "X" другой точки НИЖЕ либо на оси ординат
            y_axis_intersection = True  # Отрезок пересекает ось ординат (возвращает True)
        else:  # Иначе
            y_axis_intersection = False  # Отрезок НЕ пересекает ось ординат (возвращает False)
        return y_axis_intersection  # Возвращаем информацию о том, преесекает ли отрезок ось ординат

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


data = [Segment((2, 3), (4, 5)).length,
        Segment((1, 1), (1, 8)).length,
        Segment((0, 0), (0, 1)).length,
        Segment((15, 1), (18, 8)).length,
        Segment((-2, -3), (4, 5)).x_axis_intersection,
        Segment((-2, -3), (-4, -2)).x_axis_intersection,
        Segment((0, -3), (4, 5)).x_axis_intersection,
        Segment((2, 3), (4, 5)).y_axis_intersection,
        Segment((-2, -3), (4, 5)).y_axis_intersection,
        Segment((-2, 3), (4, 0)).y_axis_intersection
        ]


test_data = [2.83, 7.0, 1.0, 7.62, True, False, True, False, True, True]

for i, d in enumerate(data):
    assert_error = f'Не прошла проверка для метода {d.__qualname__} экземпляра с атрибутами {d.__self__.__dict__}'
    assert d() == test_data[i], assert_error
    print(f'Набор для метода {d.__qualname__} экземпляра класса с атрибутами {d.__self__.__dict__} прошёл проверку')
print('Всё ок')