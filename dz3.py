
#1. Реализовать функцию, принимающую два числа(позиционные аргументы) и
#выполняющую их деление.Числа запрашивать у пользователя, предусмотреть обработку
#ситуации деления на ноль.


def func_1(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Делить на 0 нельзя")

print(func_1(10, 0))


#2.Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон. 
#Функция должна принимать параметры как именованные аргументы. 
#Реализовать вывод данных о пользователе одной строкой.

name = input("Name: ")
surname = input("Surname: ")
phone = int(input("Phone: "))

def func(name, surname, phone):
    return ' '.join([name, surname, str(phone)])

print(func(name, surname, phone))

#3. Реализовать функцию my_func(),
#которая принимает три позиционных аргумента,
#и возвращает сумму наибольших двух аргументов.

def func(a, b, c):
    list = [a, b, c]
    #min_1 = min(list)
    list.remove(min(list))
    print(sum(list))

func(15, 8, 8)


#4. Программа принимает действительное положительное число x и целое отрицательное число y.
#Необходимо выполнить возведение числа x в степень y.
#Задание необходимо реализовать в виде функции my_func(x, y).
#При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

def sq(x, y):
    result = x ** y
    return result
x = int(input("Vvedite chislo #1 "))
y = int(input("Vvedite chislo #2 "))
a = sq(x, y)
print(a)

#6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой.
# Например, print(int_func(‘text’)) -> Text.

def int_func(s1):
    result = s1.title()
    return result
s1 = input("Vvedite text s malen'koy bukvy ")
print(int_func(s1))


