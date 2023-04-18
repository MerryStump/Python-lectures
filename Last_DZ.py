class Auto:

    def __init__(self, model, year, mark, power, color, price):
        self.__model = model
        self.__year = year
        self.__mark = mark
        self.__power = power
        self.__color = color
        self.__price = price

    def __str__(self):
        return self.__model

    def print_info(self):
        print(' Данные автомобиля '.center(40, '*'))
        print(f'\nНазвание модели: {self.__model}\nГод выпуска: {self.__year}\nПроизводитель: {self.__mark}'
              f'\nМощность двигателя: {self.__power}\nЦвет машины: {self.__color}\nЦена: {self.__price}\n')
        print('=' * 40)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, m):
        if isinstance(m, str):
            self.__model = m
        else:
            print('Ошибка')

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.__year = y

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, m):
        self.__mark = m

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, p):
        self.__power = p

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, c):
        self.__color = c

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, p):
        self.__price = p


p1 = Auto('X7 M50i', 2021, 'BMW', '530 л.с.', 'white', 10790000)
print(p1.__dict__)
p1.print_info()
print(p1.model)
p2 = Auto('2114', 2005, 'Lada', '90 л.с.', 'black', 50000)
print(p2)
