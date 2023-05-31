# Задача №27. 
# Пользователь вводит текст(строка). 
# Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. 
# Определите, сколько различных слов содержится в этом тексте.
# НЕЛЬЗЯ ИСПОЛЬЗОВАТЬ МЕТОД SPLIT

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells

# Output: 13

# text_1 ='She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'
# text_1 = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure."
# some_list = []
# print(len(text_1))
# text_1.count('sells')


text_1 = "She sells sea shells" 
# str[]
# str = text_1[0:3]
# print(str)
word = []
# j = 0
for i in range(len(text_1)-1):
    j = 0
    while text_1[i] == ' ':
        j = i
    word.append(text_1[j-i:i])
print(word)

# print(text_1[0])
# letters = [] 
# letters[0] = text_1[0]
# print(letters[0])
# for letter in text_1: 
#     letters.append(letter) 
# print(letters)
# print(len(letters))
