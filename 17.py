# Задача №17. 
# Дан список чисел. 
# Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

list_1 = [1, 1, 2, 0, -1, 3, 4, 4]
# list_1 = [1, 2, 4, 0, 1, -1, 3, 4, 4, 1, 5]
# print(list_1)
# i = 0
# j = len(list_1)-1
# n = 0
# while i <= len(list_1)-1:
#     while j >= i:
#         if list_1[i] != list_1[j]:
#             n += 1
#         j -= 1 
#     i += 1           
# print(n)
 
# на УРОКЕ
# создание списка
n = int(input('КВведите кол-во элементов: '))
some_list = []
for _ in range(n):
    some_list.append(int(input()))
print(some_list)
# решение
new_list = []
for elem in some_list:
    if elem not in new_list:
        new_list.append(elem)
print(len(new_list))