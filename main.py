# print('введите первое число: ')
# a=float(input())
# print (a)
# print(type(a))
# print(round(a,2))  
# a=-5//2
# print(a)
# d=5//2
# print(d)
# c=-5/2
# # print(c)
# k = 25 % 2
# print(k)
# r = range(100, 0, -20) # range(100, 0, -20)
# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # -5 -4 -3 -2 -1
# r = range(0, -5) # ничего не выведет
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# for i in r:
#     print(i)
# 100 80 60 40 20
# for i in 'qwerty':
#     print(i)  
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)
text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # Определить количество символов в строке:
# print('ещё' in text) # Проверить наличие символа в строке (in):
# print(text.lower()) # Функция, которая делает все буквы строки маленькими:
# print(text.upper()) # Функция, которая делает все буквы строки большими:
# print(text.replace('ещё','ЕЩЁ')) #Заменить слово на другое :
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # СъЕШЬ ещё этих МяГкИх французских булок
# print(text[:2]) # Съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих МяГкИх
# print(text[0:len(text):6]) # Сеикакл
# print(text[::6]) # Cеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
# print (text) # ЕШЬ ещёбСъ
# m = '345'
# print(m * 2) # При умножении строки на число,  она повторяется столько раз на какое была умножена
# n = 1.345 
# print(int(n)) # Отбрасывается дробная часть вне зависимости больше 0.5 или меньше
# print(int(m) * 2) # 690
# n = 1.345 
# print(str(n) * 2) # 1.3451.345
# n = '1.345' 
# print(float(n) * 2) # 2,69
# m = 2
# print(float(m)) # 2,0
# Пользователь вводит число, необходимо найти минимальный делитель данного числа
# Решение:
n = int(input())
flag = True
i = 2
while flag:
    if n % i == 0: # если остаток при делении числа n на i равен 0
        flag = False
        print(i)
    elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
        print(n)
        flag = False
    i += 1