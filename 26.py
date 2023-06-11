# Задача 26: 
# на вход принимает два числа A и B, 
# и возводит число А в целую степень B 
# с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def degree_number (c, d):
    if d == 0:
        return 1
    return c * degree_number (c, d-1)

a = int (input("Введите первое число А = "))
b = int (input("Введите второе число В = "))
print(f"A = {a}; B = {b} -> {degree_number(a, b)} ({a} в степени {b})")