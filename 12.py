# Задача 12: 
# Петя и Катя – брат и сестра. 
# Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

# num_sum = int(input('Введите первую подсказку, сумму загаданных чисел: '))
# num_composition = int(input('Введите вторую подсказку, произведение загаданных чисел: '))
# discriminant = num_sum ** 2 - 4 * num_composition

# y = num_sum // 2
# x = num_sum - y
# print(f'Число Х = {x}, число  Y = {y}')

# Пример идеального решения
x = int(input())
y = int(input())
for i in range(x):
    for j in range(y):
        if x == i + j and y == i * j:
            print(i, j)

