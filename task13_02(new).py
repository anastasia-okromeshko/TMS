# Написать свой итератор(реализовать у него и метод __next__ и __iter__), чтобы
# при обходе циклом он отдавал только элементы на четных индексах,
# возведенные в квадрат.
class ListIterator:
    def __init__(self, collection, cursor=0):
        self._collection = collection
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor >= len(self._collection):
            self._cursor = 2
            raise StopIteration()
        a = (self._collection[self._cursor]) ** 2
        self._cursor += 2
        return a


_iterable = ListIterator([1, 2, 3, 4, 5])
for i in _iterable:
    print(i)
