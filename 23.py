# Задача №23. 
# Дан массив, состоящий из целых чисел. 
# подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

# Примечание: 
# Пользователь может вводить значения
# списка или список задан изначально.


n = int(input('Введите количество элементов: '))
some_list = []
for _ in range(n):
    some_list.append(int(input()))
print(some_list)
count = 0
for i in range(1, len(some_list)):
    if some_list[i] > some_list[i-1]:
        count += 1
print(count)

