# Создать декоратор для функции, которая принимает список чисел.
# Декоратор должен производить предварительную проверку данных -
# удалять все четные элементы из списка.
def dekorator(func):
    def wrapper(a):
        a = list(filter(lambda x: int(x) % 2, a))
        return func(a)
    return wrapper


def start(my_list):
    return my_list


start = dekorator(start)
print(start([1, 2, 3, 5, 8, 10]))
