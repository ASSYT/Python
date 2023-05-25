# СПИСКИ
# Как работать со списками?
# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка
# list_1 = [7, 9, 11, 13, 15, 17]

# # чтобы вывести I элемент списка
# list_1 = [7, 9, 11, 13, 15, 17]
# print(list_1[0]) # 7

# # узнать количество элементов в списке
# list_1 = [7, 9, 11, 13, 15, 17]
# print(len(list_1)) # 6

# # заполнять во время работы
# list_1 = list() # создание пустого списка
# for i in range(5): # цикл выполнится 5 раз
# n = int(input()) # пользователь вводит целое число
# list_1.append(n) # сохранение элемента в конец списка
# print(list_1) # [12, 7, -1, 21, 0]

# # Взаимодействие цикла for со списком:
# list_1 = [12, 7, -1, 21, 0]
# for i in list_1:
#     print(i) # вывод каждого элемента списка

# list_1 = [12, 7, -1, 21, 0]
# for i in range(len(list_1)):
#     print(list_1[i]) # вывод каждого элемента списка    

# # Удаление последнего элемента списка.
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]

# # Удаление конкретного элемента из списка
list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
list_1.pop(0) # 12
print(list_1) # [7, -1, 21, 0]

# Добавление элемента на нужную позицию
# list_1 = [12, 7, -1, 21, 0]
# list_1.insert(2, 11)
# print(list_1) # [12, 7, 11, -1, 21, 0]

# КОРТЕЖИ
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t)) # class <'tuple'>
# t = (1)
# print(type(t)) # <class 'int'>
# t = (28, 9, 1990)
# print(type(t)) # class <'tuple'>
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
#     print(e) # red green blue

# Можно распаковать кортеж в независимые переменные:
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# СЛОВАРИ - неупорядоченные коллекции произвольных объектов с
# доступом по ключу.
# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←

# dictionary['left'] = '⇐'

# print(dictionary['left']) # ⇐
# print(dictionary) # {'up': '↑', 'left': '⇐', 'down': '↓', 'right': '→'}

# del dictionary['up'] # удаление элемента
# print(dictionary) #

# 1 вариант вывод в столбец ключ: значение
# for (k,v) in dictionary.items(): 
#     print(k, v)
# # 2 вариант вывод в столбец ключ: значение
# # for (item) in dictionary: 
# #     print('{}: {}'.format(item, dictionary[item]))

# # вывод в виде картежа
# print(dictionary.items())

# МНОЖЕСТВО - содержат уникальные элементы, не обязательно упорядоченные
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}

# colors.add('red') # добавить
# print(colors) # {'red', 'green', 'blue'} если есть то не добавит

# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}

# colors.clear() # { } прозрачный
# print(colors) # set() набор

# ОПЕРАЦИИ СО МНОЖЕСТВАМИ
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}

# c = a.copy() # c = {1, 2, 3, 5, 8} копирует
# print(c)

# u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21) объединяет (союз)
# print(u)

# i = a.intersection(b) # i = {8, 2, 5} пересечение (общая часть)
# print(i)

# dl = a.difference(b) # dl = {1, 3} разница a-b
# print(dl)

# dr = b.difference(a) # dr = {13, 21} разница b-a
# print(dr)

# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13} (a+b)+(a-b)
# print(q)

# a = {1, 2, 3, 5, 8}
# b = frozenset(a) # замороженный набор
# print(b) # frozenset({1, 2, 3, 5, 8})

# List comprehension - упрощенный подход к созданию списка, 
# который задействует цикл for, а также инструкции if-else 
# для определения того, что в итоге окажется в финальном списке.

# Создать список чисел от 1 до 100
# list_1 = [i for i in range(1, 101)] 
# print(list_1) # [1, 2, 3,..., 100]

# Создать список чисел от 1 до 100 только чётные числа
# list_1 = [i for i in range(1, 101) if i % 2 == 0] 
# print(list_1) # [2, 4, 6,..., 100]

#  Создать пары каждому из чисел (кортежи) чисел от 1 до 100 только чётные числа 
# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] 
# print(list_1) # [(2, 2),..., (100, 100)]

# умножать, делить, прибавлять, вычитать. Например, умножить на 2.
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]