# Задача №3. 
# Известно количество учащихся в
# каждом из трех классов. 
# Сколько минимум парт надо приобрести
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

a = int(input("Введите количество учащихся в 1 классе:"))
min_1 = a//2 +a % 2
b = int(input("Введите количество учащихся в 2 классе:"))
min_2 = b//2 + b % 2
c = int(input("Введите количество учащихся в 3 классе:"))
min_3 = c//2 +c % 2
print (f"{min_1 + min_2 + min_3} минимум парт надо приобрести")