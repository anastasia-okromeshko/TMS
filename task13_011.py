# Написать свой класс MyOpen, объекты которого должны поддерживать
# протокол контекстного менеджера. Он должен работать аналогично with
# open(‘file.txt’, ‘w+’) as f. Т.е вы можете применять его следующим образом:
# with MyOpen(file.txt’, ‘w+’) as f:
class MyOpen(object):
    def __init__(self, file_name, method):
        self.file_object = open(file_name, method)

    def __enter__(self):
        return self.file_object

    def __exit__(self, type, value, traceback):
        self.file_object.close()


with MyOpen('hello.txt', 'w+') as f:
    f.write('Hello!')
