class Animal:
    def __init__(self, name, age, color):
        self.__name = name
        self.__age = age
        self.__color = color

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        self.__color = new_color

    def play(self):
        return print('Play!')

    def eat(self):
        return print('Yum, yum')


class Music:
    def __init__(self, singer, style, volume):
        self.__singer = singer
        self.__style = style
        self.__volume = volume

    @property
    def singer(self):
        return self.__singer

    @singer.setter
    def singer(self, new_singer):
        self.__singer = new_singer

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, new_style):
        self.__style = new_style

    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = new_volume

    @property
    def off(self):
        return print('Off')

    @property
    def on(self):
        return print('On')


class Basket:
    def __init__(self, product, weight, price):
        self.__product = product
        self.__weight = weight
        self.__price = price

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, new_product):
        self.__product = new_product

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, new_weight):
        self.__weight = new_weight

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = new_price

    def check(self):
        """ Displays the text how much money did you spend
        """
        if self.__price > 50:
            return print('You spent a lot of money today')
        else:
            return print('Have a nice shopping')

    def goodbay(self):
        return print('Goodbay!')


def main():
    cat = Animal('Barsik', 2, 'black')
    cat.name = 'Mua'
    cat.play()
    print(cat.name)

    track = Music('AC/DC', 'rock', 10)
    print(track.singer, track.style, track.volume)

    purchase = Basket('Cheese', 300, 5)
    purchase.price = 60
    purchase.check()
    purchase.goodbay()


if __name__ == '__main__':
    main()
