# Картежи
# Множество
# some_set = set()
# some_set.add(1)
# some_set.add(10)
# some_set.add(30)
##
# import random
# import time
# 
# some_set = set()
# for _ in range(10 ** 6):
#     some_set.add(random.randint(100, 1100))
# some_list = list(some_set)
# 
# start = time.perf_counter()
# print(99 in some_list)
# end = time.perf_counter()
# first_duration = end - start
# 
# start = time.perf_counter()
# print(99 in some_set)
# end = time.perf_counter()
# second_duration = end - start
# print(first_duration / second_duration)
##
# СЛОВАРИ
# some_dict = {ключ: значение,}
some_dict = {'яблоко': 'apple', 'виноград': 'grape', 'банан': 'ban'}
some_dict['банан'] = 'banana'
print(some_dict['виноград'])

for i in some_dict:
    print(i, some_dict[i])

for j in some_dict.values():
    print(j)

for i in sorted(some_dict):
    print(i, some_dict[i])
