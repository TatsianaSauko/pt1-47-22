"""
Напишите программу, запрашивающую у пользователя целые числа, пока
он не оставит строку ввода пустой. После окончания ввода на экран
должны быть выведены сначала все отрицательные числа, которые были
введены, затем нулевые и только после этого положительные. Внутри
каждой группы числа должны отображаться в той последовательности,
в которой были введены пользователем.
Например, если он ввел следующие числа: 3, -4, 1, 0, -1, 0 и -2,
вывод должен оказаться таким: -4, -1, -2, 0, 0, 3 и 1. Каждое
значение должно отображаться на новой строке.
"""

list0 = []
while True:
    str1 = str(input("Введите число: "))
    if str1 == "":
        break
    else:
        list0.append(int(str1))
list1 = []
list2 = []
list3 = []
for item in range(len(list0)):
    if list0[item] < 0:
        list1.append(list0[item])
    elif list0[item] == 0:
        list2.append(list0[item])
    else:
        list3.append(list0[item])
list4 = list1 + list2 + list3
for elem in range(len(list4)):
    print(list4[elem], end=" ")
