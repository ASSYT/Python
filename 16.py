# Задача 16: 
# Cколько раз встречается число X в массиве A[1..N]. 
# Пользователь вводит
# в первой строке натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai
# Последняя строка - число X

# 5
# 1 2 3 4 5
# 3
# -> 1

# создание списка
n = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(n):
    some_list.append(int(input()))
# print(some_list)
x = int(input('Введите значение Х = '))
# count = 0
# решение 1
# for element in some_list:
#     if element == x:
#         count += 1
# print(f"-> {count} ")

# решение 2
print(some_list.count(x))