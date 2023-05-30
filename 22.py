# Задача 22: 
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.

# Пользователь вводит 2 числа. 
# n - кол-во элементов первого набора целых чисел. 
# m - кол-во элементов второго набора целых чисел. 
# Затем пользователь вводит сами элементы этих наборов.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# создание списков
n = int(input('Введите кол-во элементов первого набора целых чисел: '))
m = int(input('Введите кол-во элементов второго набора целых чисел: '))

n_list = []
m_list = []
for _ in range(n):
    n_list.append(int(input()))
print(n_list, end = ' ')
print()

for _ in range(m):
    m_list.append(int(input()))
print(m_list, end = ' ')
print()

#решение
n_multitude = set(n_list)
# print(n_multitude)
# print()

m_multitude = set(m_list)
# print(m_multitude)
# print()

nm_multitude = n_multitude.intersection(m_multitude)
# print(nm_multitude)
# print()

nm_list = list(nm_multitude)
nm_list.sort()
print(nm_list)
print()