a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = list(filter(lambda elem: elem in b, a))
print(result)

# Напишите код, который переводит целое число в строку, при том что его можно применить в любой системе счисления.
print(int('ABC', 16))

# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево
n = str(input())
if n == n[::-1]:
    print("Палиндром")
