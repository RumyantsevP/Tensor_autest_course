# I. Напишите класс PublicTransport
# Экземпляр класса создается из следующих атрибутов:
#   1. brand - Марка транспорта
#   2. ЗАЩИЩЕННЫЙ (protected) атрибут engine_power - Мощность двигателя
#   3. year - Год выпуска
#   4. color - Цвет
#   5. max_speed - Максимальная скорость
# У класса должно быть СВОЙСТВО info, которое выводить на печать информацию о:
# марке, цвете, годе выпуска и мощности двигателя
#
# II. Напишите класс Bus унаследованный от PublicTransport
# Дополнительными атрибутами будут:
#   1. passengers - кол-во пассажиров
#   2. ПРИВАТНЫЙ (private) атрибут park - Парк приписки автобуса
#   3. ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда
# Добавить свойство park, которое будет возвращать значение park
# а при присвоении проверять номер парка, что он в диапазоне от 1000 до 9999
#
# III. Напишите класс Tram унаследованный от PublicTransport
# Дополнительными атрибутами будут:
#   1. ПРИВАТНЫЙ (private) атрибут route - маршрут трамвая
#   2. path - длина маршрута
#   3. ЗАЩИЩЕННЫЙ (protected) атрибут fare - Стоимость проезда
# У класса должно быть СВОЙСТВО how_long, которое вычисляет время за прохождение маршрута по формуле max_speed/(4*path)

# Здесь пишем код
class PublicTransport:
    """
    Класс используется для:
    1. Вывода на печать информации о: марке, цвете, годе выпуска и мощности двигателя
    2. Возвращает информацию о парке приписки автобуса и при присвоении номера парка проверяет, что он в заданном диапазоне
    3. Вычисляет время, затраченное на прохождение маршрута по формуле: max_speed/(4*path)
    """
    def __init__(self, brand, engine_power, year, color, max_speed):
        """
        Инициализация данных о транспорте
        :param brand: марка транспорта
        :param engine_power: мощность двигателя
        :param year: год выпуска
        :param color: цвет
        :param max_speed: максимальная скорость
        """
        self.brand = brand  # марка транспорта (public)
        self._engine_power = engine_power  # мощность двигателя (protected)
        self.year = year  # год выпуска (public)
        self.color = color  # цвет (public)
        self.max_speed = max_speed  # максимальная скорость (public)

    @property
    def info(self):
        """
        Вывод на печать информации о транспорте
        """
        print(self.brand, self.color, self.year, self._engine_power)  # Вывод на печать марки, цвета, года выпуска, мощности двигателя

class Bus(PublicTransport):
    """
    Класс наследует атрибуты из родительского класса "PublicTransport"
    Класс используется для:
    1. Возвращение значения park
    """
    def __init__(self, brand, engine_power, year, color, max_speed, passengers, park, fare):
        """
        Инициализация данных о транспорте
        :param brand: марка транспорта
        :param engine_power: мощность двигателя
        :param year: год выпуска
        :param color: цвет
        :param max_speed: максимальная скорость
        :param passengers: кол-во пассажиров
        :param park: парк приписки автобуса
        :param fare: стоимость проезда
        """
        super().__init__(brand, engine_power, year, color, max_speed)  # Получаем доступ к методам базового класса (суперкласса)
        self.passengers = passengers  # кол-во пассажиров (public)
        self.__park = park  # парк приписки автобуса (private)
        self._fare = fare  # стоимость проезда (protected)

    @property
    def park(self):
        """
        Возвращает значение парка
        :return: значение парка
        """
        return self.__park  # Возвращаем номер парка

    @park.setter
    def park(self, park):
        assert 1000 <= park <= 9999  # Проверяем входит ли присваиваемое значение номера парка "park" в интервал от 1000 до 9999 включительно
        self.__park = park  # Присваиваем номер парка, если присваиваемое значение входит в интервал

class Tram(PublicTransport):
    """
    Класс наследует атрибуты из родительского класса "PublicTransport"
    Класс используется для:
    1. Вычисления время, за которое транспорт проходит маршрут. Вычисляется по формуле: max_speed/(4*path)
    """
    def __init__(self, brand, engine_power, year, color, max_speed, route, path, fare):
        """
        Инициализация данных о транспорте
        :param brand: марка транспорта
        :param engine_power: мощность двигателя
        :param year: год выпуска
        :param color: цвет
        :param max_speed: максимальная скорость
        :param route: маршрут трамвая
        :param path: длина маршрута
        :param fare: стоимость проезда
        """
        super().__init__(brand, engine_power, year, color, max_speed)  # Получаем доступ к методам базового класса (суперкласса)
        self.__route = route  # маршрут трамвая (private)
        self.path = path  # длина маршрута (public)
        self._fare = fare  # стоимость проезда (protected)

    @property
    def how_long(self):
        """
        Расчет времени на прохождение маршрута
        :return: время, за которое транспорт проходит маршрут. Вычисляется по формуле: max_speed/(4*path)
        """
        return self.max_speed/(4*self.path)  # Возвращаем время, за которое транспорт проходит маршрут


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ
transport = PublicTransport('Автомобиль', 500, 2040, 'Фиолетовый', 300)
first_bus = Bus('ЛиАЗ', 210, 2015, 'Зеленый', 100, 70, 1232, 32)
second_bus = Bus('VOLGABUS', 320, 2019, 'Желтый', 110, 39, 1111, 32)
first_tram = Tram('71-931M', 125, 2010, 'Красный', 75, 5, 15, 32)
second_tram = Tram('71-409-1', 240, 2018, 'Белый', 85, 7, 17, 32)

assert isinstance(type(transport).info, property), 'В классе PublicTransport, info - не свойство класса'
assert transport._engine_power, 'В классе PublicTransport, engine_power не защищенный атрибут'
assert first_bus._Bus__park, 'В классе Bus, park не приватный атрибут'
assert second_bus._fare, 'В классе Bus, fare не защищенный атрибут'
assert first_tram._fare, 'В классе Tram, fare не защищенный атрибут'
assert second_tram._Tram__route, 'В классе Tram, route не приватный атрибут'
assert isinstance(type(first_tram).how_long, property), 'В классе Tram, how_long - не свойство класса'
assert first_tram.how_long == 1.25, 'В классе Tram, how_long неверно вычисляется'
assert isinstance(type(second_bus).park, property), 'В классе Bus, park - не свойство класса'
try:
    second_bus.park = 999
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
except AssertionError:
    print('Проверка на правильность диапазона пройдена')
try:
    second_bus.park = 1234
    print('Проверка на правильность диапазона пройдена')
except AssertionError:
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
try:
    second_bus.park = 10000
    raise Exception('Проверка на ограничение диапазона НЕ пройдена')
except AssertionError:
    print('Проверка на правильность диапазона пройдена')
print('Всё ок')