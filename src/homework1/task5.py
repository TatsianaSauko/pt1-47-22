"""
Выведите n-ое число Фибоначчи, используя только временные переменные, циклические операторы
и условные операторы. n - вводится
"""

n = input("Номер элемента ряда Фибоначчи: ")
n = int(n)
F1 = 1
F2 = 1
i = 0
while i < (n - 2):
    F_sum = F1 + F2
    F1 = F2
    F2 = F_sum
    i = i + 1

print("Значение этого элемента:", F2)
