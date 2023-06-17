# Задача 38: 
# Создать телефонный справочник возможностью добавления записей и чтения. 
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи с этой фамилий. 
# Пользователь может добавлять новых людей в справочник в режиме экспорт.

def imp():
    surname = input("Введите фамилию: ")
    with open('result.txt', 'r', encoding='utf-8') as file:
        some_list = file.read().split()  # читаем данные из файла и делим строки на слова
        i = 0
        result_list = []  # создаем пустой список для записей, содержащих искомую фамилию
        while i < len(some_list): # проверяем каждый третий элемент в списке, начиная с 0-го
            if some_list[i] == surname: # если текущий элемент совпадает с искомой фамилией
                result_list.append(some_list[i:i+3]) # добавляем всю запись в список
            i += 3  # переходим к следующему третьему элементу в списке
        if result_list ==[]:
            print(f"В справочнике данных по фамилии {surname} нет")
        for record in result_list: # выводим список записей в столбик
            print(*record, sep='\n') # НАСТАВНИК пояснить

def exp():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    with open('result.txt', 'a', encoding='utf-8') as file:
        some_list = [surname, name, phone]
        for word in some_list:
            file.write('\n' + word) # курсор стоит на пустой строчке

mode = int(input("Введите режим: 1 - экспорт, 2 - импорт  "))
if mode == 1:
    exp()
elif mode == 2:
        imp()
else:
    print("Некорректный режим")
# print(mode)