"""
Определите, является ли число палиндромом (читается слева направо и справа
налево одинаково). Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в
строку или что-нибудь еще)
"""

a = int(input("Введите Ваше число: "))
c = a
i = 0
while a > 0:
    b = a % 10
    i = i * 10 + b
    a = a // 10
if c == i:
    print(f"Число {c} является полиндромом!")
else:
    print(f"Число {c} не является полиндромом!")
