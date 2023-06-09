# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., 
# где a0 = 0, a1= 1, ak= ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

 #  без рекурсии
x = int(input())
a, b = 1, 1

for i in range(0, x+1):
    if i == x:
        print(i, '=>', a)
    a, b = b, a + b
print(' ')

# с рекурсией
def fib(n):
    if (n <= 1):
        return n
    return (fib(n-1) + fib(n-2))
n = int(input("Введите число членов последовательности:"))
print(f"{n}-е число Фибоначчи => {fib(i+1)}")
# print("Последовательность Фибоначчи:")
# for i in range(1, n+1):
#     print(fib(i), end =' ')
print(' ')