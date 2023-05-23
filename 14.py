# Задача 14: 
# Требуется вывести все целые степени двойки 
# (т.е. числа вида 2 в степени k ), 
# не превосходящие числа N.

# 10 -> 1 2 4 8

# num_limit = int(input('Введите число N: '))
# print(f' {num_limit} ->', end = ' ')
# two_degree = 1
# while two_degree <= num_limit:
#     print(two_degree, end = ' ')
#     two_degree *= 2
# print()

# Примеры идеального решения
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i, end = ' ')
    i += 1
print()

