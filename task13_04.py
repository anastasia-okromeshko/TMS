# Создать класс Car. Атрибуты: марка, модель, год скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5), уменьшение
# скорости(скорость - 5), стоп(сброс скорости на 0),
# отображение скорости, разворот(изменение знака
# скорости). Все атрибуты приватные.
class Car:
    def __init__(self, brand, model, year, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model):
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year):
        self.__year = new_year

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, new_speed):
        self.__speed = new_speed

    def clock(self):
        print(self.__speed)

    def increase_speeds(self):
        """ Increases speed by 5
        """
        if self.__speed >= 0:
            return self.__speed + 5
        else:
            raise ValueError('Speed < 0')

    def decrease_speed(self):
        """ Decreases speed by 5
        """
        try:
            if self.__speed - 5 > 0:
                raise ValueError('Speed < 0')
        except ValueError as s:
            print(s)
        else:
            return self.__speed - 5

    def stop(self):
        """ Reset speed to 0
        """
        if self.__speed != 0:
            return self.__speed == 0
        else:
            raise ValueError('You go')

    def reversal_car(self):
        """ Speed sign change
        """
        if self.__speed != 0:
            return self.__speed * -1
        else:
            return print('You stop')


def main():
    car_1 = Car('BMW', '560', 2020, -5)
    print(car_1.decrease_speed())


if __name__ == '__main__':
    main()
