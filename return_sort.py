# import function_file
# print(function_file.f(1)) # Целое
# print(function_file.f(2.3)) # 23
# print(function_file.f(28)) # None

# В Python можно перемножать строку на число
# def new_string(symbol, count):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# # print(new_string('!')) # TypeError missing 1 required ...

# def new_string(symbol, count=3):
#     return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12

# # Можно указать любое количество значений аргумента функции.
# # Перед аргументом надо поставить *
# def concatenatio(*params):
#     res = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1
# # print(concatenatio(1, 2, 3, 4)) # TypeError: ...

# # Рекурсия — это функция, вызывающая сама себя.

# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1) # [1, 1, 2, 3, 5, 8, 13, 21, 34]

# x = int(input())

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# for i in range(1, x + 1):
#     print(i, '=>', fibonacci(i))

# #  без рекурсии
# x = int(input())
# a, b = 1, 1

# for i in range(1, x + 1):
#     print(i, '=>', a)
#     a, b = b, a + b

# def fibonacci(n):
#     if (n <= 1):
#         return n
#     else:
#         return (fibonacci(n-1) + fibonacci(n-2))
# n = int(input("Введите число членов последовательности:"))
# print("Последовательность Фибоначчи:")
# for i in range(n+1):
#     print(fibonacci(i))

# Быстрая сортировка
# def quicksort(array):
#     if len(array) < 2:
#         return array
#     else:
#         pivot = array[0]
#         less = [i for i in array[1:] if i <= pivot]
#         greater = [i for i in array[1:] if i > pivot]
#         return quicksort(less) + [pivot] + quicksort(greater)

# print(quicksort([5, 5, 2, 3]))

# Сортировка слиянием
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums)//2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1
# nums = [38, 27, 43, 3, 9, 82, 10]
# merge_sort(nums)
# print(nums)

# def my_func(*args): 
#     print(args) # в виде кортежа
# my_func(2, 4, key=10) # TypeError: my_func() got an unexpected keyword argument 'key'
# my_func(2, 4) #  (2, 4)

# def my_func(**kwargs): 
#     print(kwargs) # как словарь
# my_func() #  {}
# my_func(a=5, b=10, c=15) #  {'a': 5, 'b': 10, 'c': 15}
# my_func(a=5, b=10, 8) # SyntaxError: positional argument follows keyword argument

def my_func(*, a=5, b=10):
    print(a, b)
my_func()
my_func(a=2, b=3)
my_func(b=1, a=10)
my_func(a=2, b=3)
# my_func(7, b=1, a=10)