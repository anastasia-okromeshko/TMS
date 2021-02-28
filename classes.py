# Создать класс Point, описывающий точку(атрибуты: x, y). Создать класс
# Figure. Создать три дочерних класса Circle(атрибуты: координаты
# центра(тип Point), длина радиуса; методы: нахождение периметра и
# площади окружности), Triangle(атрибуты: три точки, методы: нахождение
# площади и периметра), Square(атрибуты: две точки, методы: нахождение
# площади и периметра). При потребности создавать все необходимые
# методы не описанные в задании. Создать список фигур и в цикле
# подсчитать и вывести площади всех фигур на экран[my-oop-03]
# Примечание: в рамках задание создать два файла: classes.py и
# main.py . В первом будут описаны все классы, во втором классы будут
# импортированы и использованы.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Figure:
    pass


class Circle(Figure):
    def __init__(self, x, y, l_radius):
        self.point = Point(x=x, y=y)
        self.l_radius = l_radius

    def perimeter(self):
        result_p = self.l_radius * (3.14 * 2)
        return result_p

    def square(self):
        result_s = 3.14 * (self.l_radius ** 2)
        return result_s


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        result_p = self.a + self.b + self.c
        return result_p

    def square(self):
        result_s = (self.a * self.b) / 2
        return result_s


class Square(Figure):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def perimeter(self):
        result_p = self.a * 2
        return result_p

    def square(self):
        result_s = self.a * 4
        return result_s
