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

def rhyme (phrase_1):
    some_list = []
    for word in phrase_1.split():
        suma = 0
        for letter in word:
            if letter in 'аеоэяиёуюы':
                suma += 1
        some_list.append(suma)
    return some_list     

# phrase = 'пара-ра-рам рам-пам-папам па-ра-па-да'
# phrase = 'пара-ра-рам рам-папам па-ра-па-да'
phrase = str(input("введите фразу: "))
new_list = list(map(
        lambda i: 'Парам пам-пам' 
        if len(phrase.split()) != 1 and len(rhyme(phrase)) == rhyme(phrase).count(rhyme(phrase)[0])
        else 'Пам парам', 
        rhyme (phrase)
    )
)

print(new_list[0])

