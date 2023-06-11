# def sq1(x):
#     print(x ** 2)
#
#
# print(sq1(10))
#
# def sq2(x):
#     return x ** 2
#
#
# print(sq2(20))

# def c(x):
#     return x ** 3
#
#
# some_list = [1, 2, 3, 4, 5]
#
# new_list = []
#
# for el in some_list:
#     new_list.append(c(el))
#
# print(new_list)

# some_list = [1, 2, 3, 4, 5]
# new_list = list(map(str, some_list))
# print(new_list)

# def c(x):
#     return str(x)

# some_list = [1, 2, 3, 4, 5]
# new_list = list(map(c, some_list))
# print(new_list)

# some_list = [1, 2, 3, 4, 5]
# new_list = list(map(lambda x: str(x), some_list))
# print(new_list)


# def c(x):
#     return x ** 3

fin = lambda x: x ** 2 if x % 2 == 0 else x ** 3
some_list = [1, 2, 3, 4, 5]
new_list = list(map(fin, some_list))
print(new_list[0])

# def even(a):
#     return a % 2 == 0


# some_list = [1, 2, 3, 4, 5]

# new_list = list(filter(lambda a: a % 2 == 0, some_list))
# print(new_list)

import random

# some_list = []
# for _ in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7... 99
#     number = random.randint(1, 5)
#     if number % 2 == 0:
#         some_list.append(number)
# print(some_list)
# print(len(some_list))

# some_list = [random.randint(1, 5) for _ in range(10)] # формирует рондомно 10 чисел из промежутка 1-5
# print(len(some_list))

# some_list = [int(input()) for _ in range(int(input()))]
# print(some_list)
# print(len(some_list))

