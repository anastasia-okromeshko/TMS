import time
def decorator(func):
    def wrapper(*args, **kwargs):
        time_1 = time.process_time()
        a = func(*args, **kwargs)
        print(func.__name__, time.process_time() - time_1)
        print(*args, **kwargs)
        return a
    return wrapper


@decorator
def string_1(string):
    return string


print(string_1('Hello, world'))
