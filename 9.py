# Задача №9. 
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120
# n = int(input("Введите число: "))
# result = 1
# for n in range(1,n+1):
#     result *= n
# print(result)
n = int(input("Введите значение n: "))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
 
print("Произведение всех чисел =", factorial)