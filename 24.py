# Задача 24: 
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

import time
# создание списка (грядки)
n = int(input('Введите кол-во кустов: '))
yield_list = []
for j in range(n):
    yield_list.append(int(input(f'Введите урожай каждого {j+1} куста: ')))
print(yield_list, end = ' ')
print()

# решение 1
start = time.perf_counter()
max_yield = yield_list[n-1] + yield_list[0] + yield_list[1]
for i in range (1,n-1):
    sum = yield_list[i-1] + yield_list[i] + yield_list[i+1]
    if sum >= max_yield:
        max_yield = sum 
sum = yield_list[n-2] + yield_list[n-1] + yield_list[0]
if sum >= max_yield:
    max_yield = sum
print(max_yield)
end = time.perf_counter()
first_duration = end - start

# решение 2 БЫСТРЕЕ
start = time.perf_counter()
yield_list.insert(n, yield_list[0]) 
yield_list.insert(n+1, yield_list[1])
# print(yield_list)
max_yield = yield_list[0] + yield_list[1] + yield_list[2]
for i in range (2,n+1):
    sum = yield_list[i-1] + yield_list[i] + yield_list[i+1]
    if sum >= max_yield:
        max_yield = sum 
print(max_yield)
end = time.perf_counter()
second_duration = end - start
print(first_duration / second_duration)
