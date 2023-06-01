# Задача 18: 
# Найти в массиве A[1..N] 
# самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит 
# в первой строке - натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai
# Последняя строка - содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5
import time
# создание списка
n = int(input('Введите кол-во элементов: '))
some_list = []
for _ in range(n):
    some_list.append(int(input()))
print(some_list)

# решение
some_list.sort()
print(some_list)
x = int(input('Введите значение Х = '))

# 1 var
start = time.perf_counter()
if x < some_list[0]:
    print(f'-> {some_list[0]}')
else:
    i = 1
    while x > some_list[i] and i < n-1:
        i += 1
    if abs(x-some_list[i]) >= (x-some_list[i-1]):
        print(f'-> {some_list[i-1]}')
    if abs(x-some_list[i]) <= abs(x-some_list[i-1]):
        print(f'-> {some_list[i]}')
end = time.perf_counter()
first_duration = end - start


#  2 var БЫСТРЕЕ
start = time.perf_counter()
i = 1
while x > some_list[i] and i < n-1:
    i += 1
if abs(x-some_list[i]) >= (x-some_list[i-1]):
    print(f'-> {some_list[i-1]}')
        # ind = i-1
if abs(x-some_list[i]) <= abs(x-some_list[i-1]):
    print(f'-> {some_list[i]}')
end = time.perf_counter()
second_duration = end - start
print(first_duration / second_duration)

# препод 1
count = int(input('Кол-во: '))
some_list = []
for _ in range(count):
    number = int(input())
    some_list.append(number)

# some_list = [int(input('Введите число: ')) for _ in range(int(input('Кол-во: ')))]

x = int(input('Заданное число: '))
find_number = some_list[0]
for number in some_list:
    if abs(x - number) < abs(x - find_number):
        find_number = number
print(find_number)

# препод 2
# count = int(input('Кол-во: '))
# some_set = set([int(input('Введите число: ')) for _ in range(count)])
# x = int(input('Заданное число: '))
# diff = 1
# while True:
#     if x + diff in some_set:
#         print(x + diff)
#         break
#     if x - diff in some_set:
#         print(x - diff)
#         break
#     diff += 1