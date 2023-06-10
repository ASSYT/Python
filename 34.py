# Задача 34:  
# ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой слове фразы одинаковое.
# Фраза может состоять из одного слова,
# если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами.
# Фраза вводится в программу с клавиатуры.

# Посмотреть, есть ли в фразе ритм.
# В ответе напишите:
# “Парам пам-пам”, если с ритмом все в порядке
# “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам

# def rhyme (phrase_1):
#     some_list = []
#     for word in phrase_1.split():
#         suma = 0
#         for letter in word:
#             if letter in 'аеоэяиёуюы':
#                 suma += 1
#         some_list.append(suma)        
#     return len(some_list) == some_list.count(some_list[0])

# phrase = 'пара-ра-рам рам-пам-папам па-ра-па-да'
# if rhyme(phrase):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# print(str(map (lambda i: if len(phrase.split()) == rhyme(phrase).count(rhyme(phrase)[0]): 'Парам пам-пам' else "Пам парам", rhyme(phrase))))

def litter_word(word):
    list_1 = []
    suma = 0
    for letter in word:
        if letter in 'аеоэяиёуюы':
            suma += 1
        # list_1.append(suma)        
    return suma

def rhyme (phrase_1):
    some_list = []
    for _ in range(len(phrase_1.split())):
          some_list.append(litter_word)   
    return some_list 
    # return len(some_list) == some_list.count(some_list[0])
    

phrase = 'пара-ра-рам рам-пам-папам па-ра-па-да'
new_list = list(map(
        lambda i: 'Парам пам-пам' 
        if len(rhyme(phrase)) == rhyme(phrase).count(rhyme(phrase)[0])
        else 'Пам парам', 
        rhyme (phrase)
    )
)
print(new_list[0])
# def show_result(map_object):
#     for item in map_object:
#         print(item, end=' ')
#     print('')  # for new line
# print(show_result(result))
# print(bool(filter(lambda i: rhyme(phrase), phrase.split())))
