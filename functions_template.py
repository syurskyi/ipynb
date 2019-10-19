#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Defining a function and calling it

# func

#func():
    # Текст до инструкции return
    # Возвращаемое значение
    # print("Эта инструкция никогда не будет выполнена")

# print(_())

print()
# ######################################################################################################################
# Function definitions

# print_ok
#     """ Пример функции без параметров """
#     print("Сообщение при удачно выполненной операции")

# echo m
#     """ Пример функции с параметром """
#     print(_)


# summa x y
#     """ Пример функции с параметрами,
#         возвращающей сумму двух переменных """
#     x  y

print()
# ######################################################################################################################
# Callback function

# summa x y
#     x + y

# func f a b
#     """ Через переменную f будет доступна ссылка на
#         функцию summa() """
#     f a b  # Вызываем функцию summa()

# Передаем ссылку на функцию в качестве параметра
# v  f_(s_  10 20)

# summa x y
#     """ Суммирование двух чисел """
#     x  y

# d_(summa)
# summa.__n__
# summa.__c__.c__v_
# summa.__d__

print()
# ######################################################################################################################
# Definition of functions depending on conditions
# n Введите 1 для вызова первой функции:
# __ n __ 1
#     ___ echo
#         Вы ввели число 1
# ___
#     ___ echo
#         Альтернативная функция

# echo()  # Вызываем функцию
# input()

# ___ echo
#     Вы ввели число 1

# ___ echo
#     Альтернативная функция

# echo()  # Всегда выводит "Альтернативная функция"

print()
# ######################################################################################################################
# Optional parameters

# summa x y=2  # y — необязательный параметр
#     x + y

# a - s__5
# Переменной a будет присвоено значение 7
# b - s__10 50  # Переменной b будет присвоено значение 60

# ___ summa x y
#     x + y

# print(s__10 20  # Выведет: 30

print()
# ######################################################################################################################
# Key Matching

# ___ summa x y)
#     r_ x + y
#
# print(s_(y=20 x=10))  # Сопоставление по ключам
#
# ___ summa a=2 b=3 c=4  # Все параметры являются необязательными
#     ___ a + b + c
#
# print(s_(2, 3, 20))  # Позиционное присваивание
# print(s_(c=20))  # Сопоставление по ключам
#
# print()
# ######################################################################################################################
# Example of passing values ​​from… tuple and list
# ___ summa a b c
#     r_ a + b + c
# t1, arr = (1, 2, 3), [1, 2, 3]
# print(s_(_t1))                  # Распаковываем кортеж
# print(s_(_arr))                 # Распаковываем список
# t2 = (2, 3)
# print(s_(1_ _t2))               # Можно комбинировать значения
#
# print()
# ######################################################################################################################
# Example of transferring values ​​f…the dictionary
# ___ summa a b c
#     ___ a + b + c
#
# d1 = {"a": 1, "b": 2, "c": 3}
# print(s_(__d1))  # Распаковываем словарь
# t, d2 = (1, 2), {"c": 3}
# print(s_(_t_ __d2))  # Можно комбинировать значения
#
# ___ func(a, b):
#     a, b = 20, "str"
#
#
# x, s = 80, "test"
# func(x, s)  # Значения переменных x и s не изменяются
# print(x, s)  # Выведет: 80 test
#
#
# ___ func a b
#     a_0_ b_"a"_ = "str", 800
#
# x = [1, 2, 3]  # Список
# y = {"a": 1, "b": 2}  # Словарь
# f_(x, y)  # Значения будут изменены!!!
# print(x, y)  # Выведет: ['str', 2, 3] {'a': 800, 'b': 2}
#
# print()
# ######################################################################################################################
# Passing a variable object in a function

# ___ func a b
#     a  a___  # Создаем поверхностную копию списка
#     b  b.c_  # Создаем поверхностную копию словаря
#     a_0__ b_"a"_ = "str", 800
#
# x = [1, 2, 3]  # Список
# y = {"a": 1, "b": 2}  # Словарь
# f_(x, y)  # Значения останутся прежними
# print(x, y)  # Выведет: [1, 2, 3] {'a': 1, 'b': 2}
#
# f_(x_:__ y.c_())
#
# ___ func a=[]
#     a.a_(2)
#     ___ a
#
# print(f_())  # Выведет: [2]
# print(f_())  # Выведет: [2, 2]
# print(f_())  # Выведет: [2, 2, 2]
#
# ___ func a=N_
#     # Создаем новый список, если значение равно None
#     i_ a i_ N_
#         a = __
#     a.a_(2)
#     ___ a
#
# print(f_())  # Выведет: [2]
# print(f_([1]))  # Выведет: [1, 2]
# print(f_())  # Выведет: [2]
#
# print()
# ######################################################################################################################
#  Saving transferred data in a tuple

# ___ summa__t_
#     """ Функция принимает произвольное количество параметров """
#     res = 0
#     f_ i i_ t  # Перебираем кортеж с переданными параметрами
#         r_ += i
#     ___ r_
#
# print(s_(10, 20))  # Выведет: 30
# print(s_(10, 20, 30, 40, 50, 60))  # Выведет: 210
#
# ___ summa x y=5 _t  # Комбинация параметров
#     res = x + y
#     f_ i i_ t:  # Перебираем кортеж с переданными параметрами
#         r_ += i
#     r_ r_
#
# print(s_(10))  # Выведет: 15
# print(s_(10, 20, 30, 40, 50, 60))  # Выведет: 210
#
# print()
# ######################################################################################################################
# Saving the transferred data in the dictionary

# ___ func __d
#     f_ i i_ d     # Перебираем словарь с переданными параметрами
#         print("{0} => {1}".f_ i d_i_) e_=" ")
# f_(a=1, b=2, c=3) # Выведет: a => 1 c => 3 b => 2
#
# print()
# ######################################################################################################################
# Combining parameters.

# ___ func _t __d
#     """ Функция примет любые параметры """
#     f_ i i_ t
#         print i e_=" ")
#     f_ i i_ d  # Перебираем словарь с переданными параметрами
#         print("{0} => {1}".f_i d_i_) e_=" ")
#
# f_(35, 10, a=1, b=2, c=3)  # Выведет: 35 10 a => 1 c => 3 b => 2
# f_(10)  # Выведет: 10
# f_(a=1, b=2)  # Выведет: a => 1 b => 2
#
# ___ func _t a b=10 __d
#     print t a b d
#
# f_(35, 10, a=1, c=3)  # Выведет: (35, 10) 1 10 {'c': 3}
# f_(10, a=5)  # Выведет: (10,) 5 10 {}
# f_(a=1, b=2)  # Выведет: () 1 2 {}
# f_(1, 2, 3)  # Ошибка. Параметр a обязателен!
#
# ___ func x=1 y=2 * a b=10
#     print x y a b
#
# f_(35, 10, a=1)  # Выведет: 35 10 1 10
# f_(10, a=5)  # Выведет: 10 2 5 10
# f_(a=1, b=2)  # Выведет: 1 2 1 2
# f_(a=1, y=8, x=7)  # Выведет: 7 8 1 10
# f_(1, 2, 3)  # Ошибка. Параметр a обязателен!
#
# print()
# ######################################################################################################################
#  An example of using anonymous functions

# f1 = l_: 10 + 20                # Функция без параметров
# f2 = l_ x_ y_ x + y             # Функция с двумя параметрами
# f3 = l_ x y z_ x + y + z      # Функция с тремя параметрами
# print(f1())                         # Выведет: 30
# print(f2(5, 10))                    # Выведет: 15
# print(f3(5, 10, 30))                # Выведет: 45
# print()
# ######################################################################################################################
# Optional parameters in anonymous functions

# f = l_ x y=2_ x + y
# print(f(5))                         # Выведет: 7
# print(f(5, 6))                      # Выведет: 11
#
# print()
# ######################################################################################################################
# An example of using function generators

# ___ func x y
#     f_ i i_ r_ 1 x+1
#         y_ i ** y
# f_ n i_ f_ 10 2
#     print n e_=" "    # Выведет: 1 4 9 16 25 36 49 64 81 100
# print()                  # Вставляем пустую строку
# f_ n i_ f_ 10 3
#     print n e_=" "    # Выведет: 1 8 27 64 125 216 343 512 729 1000
#
# print()
# ######################################################################################################################
#  Using the __next __ () parameter

def func(x, y):
    for i in range(1, x + 1):
        yield i ** y


i = func(3, 3)
print(i.__next__())  # Выведет: 1 (1 ** 3)
print(i.__next__())  # Выведет: 8 (2 ** 3)
print(i.__next__())  # Выведет: 27 (3 ** 3)
print(i.__next__())  # Исключение StopIteration

print()
# ######################################################################################################################
#  Calling one generator function fro… (simple case)

def gen(l):
    for e in l:
        yield from range(1, e + 1)


l = [5, 10]
for i in gen([5, 10]): print(i, end = " ")

print()
# ######################################################################################################################
# Calling one function generator fro…er (hard case)

def gen2(n):
    for e in range(1, n + 1):
        yield e * 2


def gen(l):
    for e in l:
        yield from gen2(e)


l = [5, 10]
for i in gen([5, 10]): print(i, end = " ")

print()
# ######################################################################################################################
# Specifying multiple decorators

def deco1(f):
    print("Вызвана функция deco1()")
    return f
def deco2(f):
    print("Вызвана функция deco2()")
    return f
@deco1
@deco2
def func(x):
    return "x = {0}".format(x)
print(func(10))

print()
# ######################################################################################################################
# Access restriction using decorator

# passw i_ Введите пароль:
#
# ___ test_passw
#     ___ deco f
#         i_ p == "10":  # Сравниваем пароли
#             r_ f
#         e_
#             r_ l_ "Доступ закрыт"
#
#     r_ d_  # Возвращаем функцию-декоратор
#
# _test_passw passw
# ___ func
#     ___ "Доступ открыт"
#
# print(f_())  # Вызываем функцию
#
# print()
# ######################################################################################################################
# Function
# Python Scope Basics

# X = 99
#
# ___ func
#     X = 88
#
# # Global scope
# X = 99  # X and func assigned in module: global
#
# ___ func  # Y and Z assigned in function: locals
#     # Local scope
#     Z = X + Y  # X is a global
#     ___ Z
#
# print(f_(1))  # func in module: result=100
#
# print()
# ######################################################################################################################
# The global Statement

# X = 88  # Global X
#
# ___ func
#     g_ X
#     X = 99  # Global X: outside def
#
# func()
# print(X)  # Prints 99
#
# y, z = 1, 2  # Global variables in module
#
# ___ all_global
#     g___ x  # Declare globals assigned
#     x = y + z  # No need to declare y, z: LEGB rule
#
# print()
# ######################################################################################################################
# Scopes and Nested Functions

# X = 99  # Global scope name: not used
# print(X)
#
# ___ f1
#     X = 88  # Enclosing def local
#
#     ___ f2
#         print(X)  # Reference made in nested def
#
#     f2()
#
# f1()  # Prints 88: enclosing def local
#
# ___ f1
#     X = 89
#
#     ___ f2
#         print(X)  # Remembers X in enclosing def scope
#
#     ___ f2  # Return f2 but don't call it
#
#
# action = f1()  # Make, return function
# action()  # Call it now: prints 88
#
# print()
# ######################################################################################################################
# Retaining Enclosing Scope State with Defaults

# ___ f1
#     x = 88
#
#     ___ f2_x_x  # Remember enclosing scope X with defaults
#         print(x)
#
#     f2()
#
# f1()  # Prints 88
#
#
# ___ f1
#     x = 88  # Pass x along instead of nesting
#     f2(x)  # Forward reference okay
#
# ___ f2 x
#     print(x)
#
# f1()

print()
# ######################################################################################################################
# Nested scopes, defaults, and lambdas

# ___ func
#     x = 4
#     action = l_ n x ** n  # x remembered from enclosing def
#     ___ a_
#
# x f_
# print(x(2))  # Prints 16, 4 ** 2
#
# ___ func
#     x = 4
#     action = l_ n x_x x ** n  # Pass x in manually
#     ___ a_

# print()
# ######################################################################################################################
# nonlocal in Action

# ___ tester start
#     state = start  # Referencing nonlocals works normally

    # ___ nested label
    #     print l_, s_)  # Remembers state in enclosing scope
    # ___ n_

# F = t_(0)
# F('spam')
# F('ham')

# ___ tester start
#     state = start

    # ___ nested label
    #     print l_ s_
    #     s_ += 1  # Cannot change by default (or in 2.6)

    # ___ n_

# F = t_(0)
# F('spam')  # UnboundLocalError: local variable 'state' referenced before assignment

# print()
# ######################################################################################################################
# Using nonlocal for changes

# ___ tester start
#     state = start  # Each call gets its own state

    # ___ nested label
    #     n______
    #     s___  # Remembers state in enclosing scope
    #     print(l_, s_)
    #     s_ __ 1  # Allowed to change it if nonlocal
    # ____ n_

# F = t_(0)

# print('#' * 52 + ' Increments state on each call')
# F('spam')  # Increments state on each call
# F('ham')
# F('eggs')

# print('#' * 52 + ' Make a new tester that starts at 42')
# G = t__42  # Make a new tester that starts at 42
# G__spam

# print('#' * 52 + ' My state information updated to 43')
# G__eggs  # My state information updated to 43

# print('#' * 52 + ' ')
# F__bacon  # But F's is where it left off: at 3
# Each call has different state information

print()
# ######################################################################################################################
# Arguments and Shared References

# ___ f_a_  # a is assigned to (references) passed object
#     a = 99  # Changes local variable a only

b = 88
# f(b)  # a and b both reference same 88 initially
# print(b)  # b is not changed

# ___ changer a b  # Arguments assigned references to objects
#     a = 2  # Changes local name's value only
    # b_0_  'spam'  # Changes shared object in-place

X = 1
L = [1, 2]  # Caller
# c_(X, L)  # Pass immutable and mutable objects
# X, L  # X is unchanged, L is different!

X = 1
a = X  # They share the same object
a = 2  # Resets 'a' only, 'X' is still 1
# print(X)

L = [1, 2]
# b = L  # They share the same object
# b_0_ _ 'spam'  # In-place change: 'L' sees the change too
# print(L)

print()
# ######################################################################################################################
# Avoiding Mutable Argument Changes

# changer a b
#     a = 2
#     b_0_ = 'spam'

X = 1

L = [1, 2]
# c__X L_:_  # Pass a copy, so our 'L' does not change

# print(X)
# print(L)

# changer a b
#     b _ b_ _ _  # Copy input list so we don't impact caller
#     a = 2
#     b_0_ = 'spam'  # Changes our list copy only


L = [1, 2]
# changer(X, tuple(L))    # Pass a tuple, so changes are errors

print()
# ######################################################################################################################
# Simulating Output Parameters and Multiple Results

# multiple x y
#     x = 2  # Changes local names only
#     y = [3, 4]
#     x, y  # Return new values in a tuple

X = 1
L = [1, 2]

# X, L = _(X, L)  # Assign results to caller's names
# print(X, L)

print()
# ######################################################################################################################


