# Задача 4: 
# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно:
# Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

sum = int(input("Петя, Катя и Сережа сделали всего бумажных журавликов S = "))
print (f'Сережа и Петя сделали по {sum // 6}, а Катя сделала {sum // 6 * 4}')