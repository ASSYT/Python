# 25. 
# принимает на вход строку,
# ивыводит на экран кол-во повторений каждого из символов

# Ввод: как дела
"""k - 2
    а - 2
    д - 1
    е - 1
    л - 1
"""

some_dict = {}
word = input()
for letter in word:
    if letter not in some_dict:
        some_dict[letter] = 1
    else:
        some_dict[letter] += 1
print(some_dict)