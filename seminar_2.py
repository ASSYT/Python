# Вводятся числа, пока не введут 0. Найти произведение чисел, оканчивающихся на 4.
# mult = 1
# number = int(input())
# while number != 0:
#     if number % 10 == 4:
#         mult *= number
#     number = int(input())
# if mult == 1:
#     mult = 0
# print(mult)

# Вводятся строки, пока не будет введена пустая строка. Если длина очередного введеного слова равна 5, то
# нужно вывести сообщение "YES" и прекратить возможность ввода для пользователя, если таких слов нет, то
# вывести 'NO' один раз в конце.

# flag = True
# while True:
#     some_str = input()
#     # if some_str == '':
#     #     break
#     if not some_str:
#         break
#     if len(some_str) == 5:
#         print('YES')
#         flag = False
#         break
# if flag:
#     print('NO')
# 2 вариант
some_str = input()
while some_str:
    if len(some_str) == 5:
        print('YES')
        break
    some_str = input()
else:
    print('NO')

# for _ in range(100): print("Hello") # 1 вариант
# for i in range(100): print("Hello")  # 2 вариант 

# Вводится количество чисел, затем сами числа, если число = 10, вывести YES и закончить ввод,
# в конце вывести NO если никакое из чисел не было равно 10.
# n = int(input('Введите кол-во чисел: '))
# for _ in range(n):
#     number = int(input())
#     if number == 10:
#         print('YES')
#         break
# else:
#     print('NO')