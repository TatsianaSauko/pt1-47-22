"""
Даны два списка чисел. Посчитайте, сколько различных чисел входит только в один
из этих списков (например, есть в первом списке, но нет во втором).
"""

list_1 = {int(item) for item in input("Введите 1 список ч/з пробел: ").split()}
list_2 = {int(item) for item in input("Введите 2 список ч/з пробел: ").split()}
list_new_1 = list(list_1 - list_2)
list_new_2 = list(list_2 - list_1)
print(f"1-ый список содержит {len(list_new_1)} чисел, которые не входят во 2-й")
print(f"2-ой список содержит {len(list_new_2)} чисел, которые не входят в 1-ый")
