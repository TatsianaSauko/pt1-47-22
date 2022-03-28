"""
Каждый химический элемент из таблицы Менделеева характеризуется своим
обозначением, состоящим из одного, двух или трех символов. Есть такая игра –
пытаться выразить то или иное слово через химические элементы. Например, слово
silicon может быть записано при помощи следующих химических элементов: Si, Li,
C, O и N. В то же время слово hydrogen не может быть составлено из названий
элементов.
Напишите рекурсивную функцию, способную определять, можно ли выразить переданное
ей слово исключительно через обозначения химических элементов. Ваша функция
должна принимать два параметра: слово, которое нужно проверить, и список
символов, которые можно при этом использовать. Возвращать функция должна строку,
состоящую из использованных символов, если собрать искомое слово можно, и пустую
строку в противном случае. При этом регистры символов учитываться не должны.
В основной программе должна быть использована ваша функция для проверки всех
элементов таблицы Менделеева на возможность составить их названия из обозначений
химических элементов. Отобразите на экране названия элементов вместе с
обозначениями, которые были использованы для их написания. Например, одна из
строчек может выглядеть так:
Silver может быть представлен как SiLvEr
Для решения задачи используйте набором данных с химическими элементами,
который находится в файле elements.txt.
"""


def replace_elements(str_input, elements):
    """Определяет можно ли выразить слово через обозначения химических элементов

    :param str_input: Переданное слово
    :param elements: Список химических элементов
    :return: Слово, представленное через обозначения химических элементов

    """
    for size in (3, 2, 1):
        starting = str_input[:size].capitalize()
        if starting not in elements:
            continue
        if len(str_input) == size:
            return starting
        ending = replace_elements(str_input[size:], elements)
        if ending:
            return starting + ending


try:
    with open('elements.txt') as t:
        str_in = t.read().split()
except FileNotFoundError:
    print("Ошибка при работе с файлом")
list_split = [x.split(",") for x in str_in]
list_elements = [x[1] for x in list_split]

string_input = input("Введите слово: ")
print(replace_elements(string_input, list_elements))
