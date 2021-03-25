class ListIterator:
    def __init__(self, collection, cursor=0):
        self._collection = collection
        self._cursor = cursor

    def __iter__(self):
        return self

    def __next__(self):
        if self._cursor >= len(self._collection):
            raise StopIteration()
        elif self._cursor % 2 != 0:
            print(self._collection[self._cursor])
            self._cursor += 2
        return print(self._collection[self._cursor])


_iterable = ListIterator([1, 2, 3, 4, 5])
for i in _iterable:
    print(i)
