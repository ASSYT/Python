# Задача 2: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

three_digit = int(input("Введите трехзначное число: "))
two_digit = three_digit // 10
num3 = three_digit % 10 
num1 = three_digit // 100 
num2 = two_digit % 10
print (f'Сумма цифр числа {three_digit} -> {num1 + num2 + num3} ({num1} + {num2} + {num3})')