# Написать генератор, который будет принимать на вход имя файла и
# генерировать построчно(т.е yield каждой строки).
def read_file():
    with open('hello.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield line


a = read_file()
print(next(a))
print(next(a))
