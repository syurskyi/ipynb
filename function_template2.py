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
# Keywords

def f(a, b, c): print(a, b, c)


f(1, 2, 3)

f(c=3, b=2, a=1)

f(1, c=3, b=2)


def func(name='Bob', age=40, job='dev'): print(name, age, job)


func('Serg,', 40, ', nuker')

print()
# ######################################################################################################################
# Defaults

def f(a, b=2, c=3): print(a, b, c)


f(1)

f(a=1)

f(1, 4)

f(1, 4, 5)

f(1, c=6)

print()
# ######################################################################################################################
# _combining keywords and defaults

def func(spam, eggs, toast=0, ham=0):  # First 2 required
    print((spam, eggs, toast, ham))


func(1, 2)  # Output: (1, 2, 0, 0)
func(1, ham=1, eggs=0)  # Output: (1, 0, 0, 1)
func(spam=1, eggs=0)  # Output: (1, 0, 0, 0)
func(toast=1, eggs=2, spam=3)  # Output: (3, 2, 1, 0)
func(1, 2, 3, 4)  # Output: (1, 2, 3, 4)

print()
# ######################################################################################################################
# Applying functions generically

def func(a, b, c, d): print(a, b, c, d)


args = (2, 3)
args += (4, 5)
print(args)
func(*args)


def tracer(func, *pargs, **kargs):  # Accept arbitrary arguments
    print('calling:', func.__name__)
    return func(*pargs, **kargs)  # Pass along arbitrary arguments


def func(a, b, c, d):
    return (a, b, c, d)


# def func(a, b, c, d):
#    return a + b + c + d

print(tracer(func, 1, 2, c=3, d=4))

print()
# ######################################################################################################################
# Python 3.X Keyword-Only Arguments

def kwonly(a, *b, c):
    print(a, b, c)


kwonly(1, 2, c=3)
kwonly(a=1, c=3)


def kwonly(a, *, b, c):
    print(a, b, c)


kwonly(1, c=3, b=2)
kwonly(c=3, b=2, a=1)


def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)


kwonly(1)
kwonly(1, c=3)
kwonly(a=1)
kwonly(c=3, b=2, a=1)


def kwonly(a, *, b, c='spam'):
    print(a, b, c)


kwonly(1, b='eggs')


def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)


kwonly(3, c=4)
kwonly(3, c=4, b=5)

print()
# ######################################################################################################################
# Ordering rules
# Collect args in header

def f(a, *b, c=6, **d): print(a, b, c, d)

print()
# ######################################################################################################################
# Ordering rules
#  Default used

def f(a, *b, c=6, **d)
f(1, 2, 3, x=4, y=5)

print()
# ######################################################################################################################
# Ordering rules
#  Override default

def f(a, *b, c=6, **d)
f(1, 2, 3, x=4, y=5, c=7)

print()
# ######################################################################################################################
# Ordering rules
# Anywhere in keywords

def f(a, *b, c=6, **d)
f(1, 2, 3, c=7, x=4, y=5)

print()
# ######################################################################################################################
# Ordering rules
# c is not keyword-only

def f(a, *b, c=6, **d)
def f(a, c=6, *b, **d): print(a, b, c, d)

print()
# ######################################################################################################################
# Ordering rules
# KW-only between * and **

def f(a, *b, c=6, **d): print(a, b, c, d)

print()
# ######################################################################################################################
# Ordering rules
# Unpack args at call

def f(a, *b, c=6, **d)
f(1, *(2, 3), **dict(x=4, y=5))

print()
# ######################################################################################################################
# Ordering rules
# Override default

def f(a, *b, c=6, **d)
f(1, *(2, 3), c=7, **dict(x=4, y=5))

print()
# ######################################################################################################################
# Ordering rules
# After or before *

def f(a, *b, c=6, **d)
f(1, c=7, *(2, 3), **dict(x=4, y=5))

print()
# ######################################################################################################################
# Ordering rules
# Keyword-only in

def f(a, *b, c=6, **d)
f(1, *(2, 3), **dict(x=4, y=5, c=7))

print()
# ######################################################################################################################
# Recursive Functions

def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])  # Call myself


def main():
    print(mysum([1, 2, 3, 4, 5]))

print()
# ######################################################################################################################
# Recursive Functions

def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])  # Call myself


def main():
    print(mysum([1, 2, 3, 4, 5]))

print()
# ######################################################################################################################
# Recursive Functions

def mysum(L):
    if not L: return 0
    return nonempty(L)  # Call a function that calls me


def nonempty(L):
    return L[0] + mysum(L[1:])  # Indirectly recursive


def main():
    print(mysum([1.1, 2.2, 3.3, 4.4]))

print()
# ######################################################################################################################
# Indirect Function Call

def echo(message):  # Name echo assigned to function object
    print(message)


echo('Direct call')

x = echo  # Now x references the function too
x('Indirect call!')  # Call object through name by adding ()


def indirect(func, arg):
    func(arg)  # Call the passed-in object by adding ()


indirect(echo, 'Argument call!')  # Pass the function to another function

print()
# ######################################################################################################################
# Functions can receive keyword arguments

def has_keywords(my=True, name='computer'):
    if my:
        print('My', name)
    else:
        print('Not mine', name)


has_keywords(name='phone')

print()
# ######################################################################################################################
# Function can receive unlimited number of positional arguments

def has_args(*args):
    print('A lot of arguments: ', args)


has_args(1, 'demo', [1, 2], (9, 'string'))

print()
# ######################################################################################################################
# Functions can receive unlimited number of keyword arguments

def has_kwargs(**kwargs):
    print('A lot of keyword arguments', kwargs)
    print('kwargs is a dict', type(kwargs))


has_kwargs(any_possible=None, values=[], you_wish=1)

print()
# ######################################################################################################################
# Function that will cover 100% of arguments

def send_anything(*args, **kwargs):
    print('args', args)
    print('kwargs', kwargs)


send_anything(1, 15, 'a', value=True, new_value=False)

print()
# ######################################################################################################################
# Functions can use global variables

GLOBAL_VAR = 3


def using_global_var(x):
    print(x * GLOBAL_VAR)


using_global_var(12)

print()
# ######################################################################################################################
# Functions can use global variables
# But if we want to write to it, we should state it explicitly

def writing_to_global_var(value):
    global GLOBAL_VAR
    GLOBAL_VAR = value
    print('it is now', GLOBAL_VAR)


writing_to_global_var(9)

print()
# ######################################################################################################################
# Functions are objects and can be nested

def outer_function(value):
    def some_inner():
        print('Value was', value)

    return some_inner


v = outer_function('some')
print('it is a function', v, callable(v))
v()  # 'some' will be printed

print()
# ######################################################################################################################
#  map

def work(value):
    return value * 2


t = [1, 2, 10]
m = map(work, t)
print(m)

print()
# ######################################################################################################################
# map  but using lambda function

m1 = map(lambda x: x * 2, t)
print(list(m1))

print()
# ######################################################################################################################
# filter

print(list(filter(lambda v: v > 0, [-1, -5, -9, 20, 3, 0])))

print()
# ######################################################################################################################
# reduce

from functools import reduce

r = [1, 4, 2, 3]

result = reduce(lambda x, y: x + y, r)
print(result)

print()
# ######################################################################################################################
# functions_are_objects

def my_function():
    print('I am a function')


print('Functions are objects', isinstance(my_function, object))

print()
# ######################################################################################################################
# You can pass functions as parameters

def call_passed_function(incoming):
    print('Calling!')
    incoming()
    print('Called!')


call_passed_function(my_function)

print()
# ######################################################################################################################
# You can check if something could be called

print(callable(len), callable(45), callable(callable))

print()
# ######################################################################################################################
# You can return function from a function

def return_min_function():
    return min


test = return_min_function()
min_value = test(4, 5, -9, 12)
print('Min values is', min_value)

print()
# ######################################################################################################################
#  Объявление функции hello_world

# Объявление функции hello_world
def hello_world():
    print('Hello, World!')


# Вызов функции hello_world
hello_world()

print()
# ######################################################################################################################
# procedure-with-parameter

# limit - формальный параметр функции print_numbers
def print_numbers(limit):
    for i in range(limit):
        print(i)


# Здесь вызывается функция print_numbers, а её формальный
# параметр limit замещается фактическим параметром 10
print_numbers(10)

print()
# ######################################################################################################################
# using-builtin-functions

# Функция из прошлого примера
def print_numbers(limit):
    for i in range(limit):
        print(i)


# Читаем ввод пользователя при помощи стандартной
# функции input, конструируем из него число при
# помощи стандартной функции int и записываем в
# переменную n
n = int(input('Введите n: '))
# Вызываем функцию print_numbers с фактическим параметром n
print_numbers(n)

print()
# ######################################################################################################################
# multiple-functions

# Функция из прошлого примера
def print_numbers(limit):
    for i in range(limit):
        print(i)


# Любое логически завершённое действие следует помещать в функцию
def main():
    n = int(input('Введите n: '))
    print_numbers(n)


# Вызов главной функции
main()

print()
# ######################################################################################################################
# main-function

def main():
    print('Hello, World!')


# Главную функцию желательно вызывать так
# (таким образом функция будет вызвана только если
# данный файл был запущен как главный; это важно
# для приложений, состоящих из нескольких модулей)
if __name__ == '__main__':
    main()

print()
# ######################################################################################################################
# simple-function

def add_numbers(a, b):
    return a + b  # возврат суммы параметров


x = add_numbers(2, 3)
print(x)

print()
# ######################################################################################################################
# procedures-as-functions

def procedure():
    print('I return nothing... Or I do?')


value = procedure()
print('Результат функции:', value)

print()
# ######################################################################################################################
# multiple-return-statements

# Эта функция возвращает аргумент, умноженный на два,
# если он отрицательный, или аргумент, умноженный на три,
# если он больше или равен нулю
def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3


def main():
    # Вывод значений функции в диапазоне [-3, 3]
    for i in range(-3, 4):
        y = function(i)
        print('function(', i, ') = ', y, sep='')


if __name__ == '__main__':
    main()

print()
# ######################################################################################################################
# return-in-procedures

def hello(name):
    # Если имя пустое, выходим из функции
    if not name:
        return
    print('Hello, ', name, '!', sep='')


hello('Alex')
hello('')
hello('Python')

print()
# ######################################################################################################################
# functions-in-expressions

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


# Вызов функции может быть частью выражения
print(add(2, 3) + sub(2, 3))  # => print((2 + 3) + (2 - 3))

print()
# ######################################################################################################################
# keyword-arguments

# Функция, которая принимает три аргумента
def info(object, color, price):
    print('Объект:', object)
    print('Цвет:', color)
    print('Цена:', price)
    print()


# передача параметров в прямом порядке
info('ручка', 'синий', 1)
# передача параметров в произвольном порядке
info(price=5, object='чашка', color='оранжевый')
# можно смешивать оба способа, но сначала должны идти параметры,
# которые передаются в прямом порядке
info('кофе', price=10, color='чёрный')

print()
# ######################################################################################################################
# optional-arguments

# Если параметр name не задан, то name = 'Alex'
def hello(name='Alex'):
    print('Hello, ', name, '!', sep='')


hello('Python')
hello()

print()
# ######################################################################################################################
# functions_as_first_class_objects

# Создание ссылки на объект
out = print
out('Hello')


# Сохранение ссылок на функции в структуре данных

def add(x, y):
    return x + y


def sub(x, y):
    return x - y


operations = {
    '+': add,
    '-': sub
}

print(operations['+'](2, 3))
print(operations['-'](2, 3))

print()
# ######################################################################################################################
# lambda_expressions

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y
}

print(operations['+'](2, 3))
print(operations['-'](2, 3))

print()
# ######################################################################################################################
# closures

﻿"""Пример замыкания"""


def make_closure():
    variable = 42

    def closure():
        return variable

    return closure


fn = make_closure()
print(fn())

print()
# ######################################################################################################################
# advanced_closure_example

"""Демонстрация часто допускаемой ошибки и способа её решения"""


def make_powers(n):
    """Функция, возвращающая список функций, каждая из которых вычисляет
    степень аргумента, равную данному индексу плюс 1
    (неправильная реализация)
    """

    functions = []

    for i in range(1, n + 1):
        functions.append(lambda x: x ** i)

    return functions


for function in make_powers(3):
    print(function(2))

# Видно, что результататом было не 2, 4, 8, как можно было бы ожидать,
# а 8, 8, 8

print()


# Причиной этого является так называемое позднее связываение.  К тому моменту,
# когда вызываются функции из списка, цикл в функции make_powers уже выполнен и
# переменная i всегда равна n + 1.

# Для того, чтобы избавиться от этого, необходимо скопировать данную переменную
# в локальные переменные каждой функции.  Единственный способ создать локальную
# переменную в лямбда-выражении -- это создать параметр функции.

def make_powers(n):
    """Функция, возвращающая список функций, каждая из которых вычисляет
    степень аргумента, равную данному индексу плюс 1"""

print()
# ######################################################################################################################
# Пример каррирования функции

def ordinary_add(x, y):
    """Обычная функция"""
    return x + y


def curryied_add(x):
    """Каррированная функция"""

    def do_add(y):
        return x + y

    return do_add


print(ordinary_add(2, 3))
print(curryied_add(2)(3))

# Каррирование делает лёгким частичное применение функций
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))

print()

# В виде лямбда-выражений
ordinary_add = lambda x, y: x + y
curryied_add = lambda x: lambda y: x + y

print(ordinary_add(2, 3))
print(curryied_add(2)(3))
add_to_five = curryied_add(5)
print(add_to_five(2))
print(add_to_five(3))

print()
# ######################################################################################################################
# decorator

def decorator(fn):
    """Пример декоратора"""

    def decorated_fn(*args, **kwargs):
        """Модифицированная функция"""

        print('Decorated function says:')
        fn(*args, **kwargs)  # вызов изначальной функции
        print()

    return decorated_fn


@decorator
def hello():
    print('Hello!')


# Вызов декорированной функции
hello()

print()
# ######################################################################################################################
# Пример создания декоратора с параметром

def cast_result(type_):
    """Пример создания декоратора с параметром"""

    def cast_decorator(function):
        """Сам декоратор"""

        def decorated_function(*args, **kwargs):
            result = function(*args, **kwargs)
            return type_(result)

        return decorated_function

    return cast_decorator


@cast_result(float)
def add(x, y):
    return x + y


print(add(2, 3))

import decimal


@cast_result(repr)
@cast_result(decimal.Decimal)
def div(x, y):
    return x / y


print(div(3, 2))

print()
# ######################################################################################################################
# Пример использования функции map

string = '2 4 8 15 42'
numbers = map(int, string.split())
print(list(numbers))

print()
# ######################################################################################################################
# Пример использования функции filter

numbers = [3, 2, -1, 0, 15, -8, -7, 3, -3, 8]
positive_numbers = filter(lambda x: x > 0, numbers)
print(list(positive_numbers))

print()
# ######################################################################################################################
# Пример использования функции reduce

from functools import reduce

numbers = [3, 2, 1, 8, -3, -2]
# Произведение всех чисел списка
product = reduce(lambda x, y: x * y, numbers)

print(product)

print()
# ######################################################################################################################
# lru_cache

from functools import lru_cache


# Здесь функция вычисления чисел Фибоначчи записана рекурсивно, но по
# произоводительности и расходу памяти она будет сравнима с нерекурсивной
@lru_cache(maxsize=None)
def fibonacci(index):
    if index < 2:
        return 1
    else:
        return fibonacci(index - 1) + fibonacci(index - 2)


for i in range(1, 1000):
    print(fibonacci(i))

print()
# ######################################################################################################################
# partial

from functools import partial

# Частичное применение функции
print_with_comma = partial(print, sep=', ')

print_with_comma(2, 3, 5)

print()
# ######################################################################################################################
# Пример использования комбинаторных генераторов модуля itertools

from itertools import permutations, combinations, combinations_with_replacement

print(list(permutations('ABC', 2)))
print()

print(list(combinations('ABC', 2)))
print()

print(list(combinations_with_replacement('ABC', 2)))

print()
# ######################################################################################################################
# Пример использования функции product модуля itertools

from itertools import product

for a, b in product(range(2), range(3)):
    print(a, b)

print()
# ######################################################################################################################
# Positional Arguments

def my_func(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))

print()
# ######################################################################################################################
# Default Values

# Note that once a parameter is assigned a default value, all parameters thereafter must be asigned a default value too!

def my_func(a, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))


my_func(10, 20, 30)
my_func(10, 20)
my_func(10)

Since a does not have a default value, it must be specified:

print()
# ######################################################################################################################
# Keyword Arguments (named arguments)

def my_func(a, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))

my_func(c=30, b=20, a=10)
my_func(10, c=30, b=20)


# Note that once a keyword argument has been used, all arguments thereafter must also be named:
#
# However, if a parameter has a default value, it can be omitted from the argument list, named or not:


my_func(10, c=30)
my_func(a=30, c=10)
my_func(c=10, a=30)

print()
# ######################################################################################################################
#  arbitrary numbers of positional parameters/arguments:

def func1(a, b, *args):
    print(a)
    print(b)
    print(args)

func1(1, 2, 'a', 'b')

# A few things to note:
# Unlike iterable unpacking, *args will be a tuple, not a list.
# The name of the parameter args can be anything you prefer
# You cannot specify positional arguments after the *args parameter - this does something different that we'll cover in the next lecture.

print()
# ######################################################################################################################
# how we might use this to calculate the average of an arbitrary number of parameters.

def avg(*args):
    count = len(args)
    total = sum(args)
    return total/count


avg(2, 2, 4, 4)

avg() # error

def avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count

avg(2, 2, 4, 4)
avg()

# But we may not want to allow specifying zero arguments, in which case we can split our parameters into a required (non-defaulted) positional argument, and the rest:

def avg(a, *args):
    count = len(args) + 1
    total = a + sum(args)
    return total/count

avg(2, 2, 4, 4)

avg()

print()
# ######################################################################################################################
# Unpacking an iterable into positional arguments

def func1(a, b, c):
    print(a)
    print(b)
    print(c)


l = [10, 20, 30]

The function expects three positional arguments, but we only supplied a single one (albeit a list).

But we could unpack the list, and then pass it to as the function arguments:

func1(*l)

print()
# ######################################################################################################################
# To make the keyword argument optional, we just need to specify a default value in the function definition:

def func1(*args, d='n/a'):
    print(args)
    print(d)


func1(1, 2, 3)
func1()

print()
# ######################################################################################################################
# Sometimes we want only keyword arguments, in which case we still have to exhaust the positional arguments first -
# but we can use the following syntax if we do not want any positional parameters passed in:

def func1(*, d='hello'):
    print(d)

func1(10, d='bye')
func1(d='bye')

print()
# ######################################################################################################################
# We can also include positional non-defaulted (first), positional defaulted (after positional non-defaulted)
# followed lastly (after exhausting positional arguments) by keyword args (defaulted or non-defaulted in any order)

def func1(a, b=20, *args, d=0, e='n/a'):
    print(a, b, args, d, e)

func1(5, 4, 3, 2, 1, d=0, e='all engines running')

func1(0, 600, d='goooood morning', e='python!')

func1(11, 'm/s', 24, 'mph', d='unladen', e='swallow')

print()
# ######################################################################################################################
# **kwargs

def func(**kwargs):
    print(kwargs)

func(x=100, y=200)

print()
# ######################################################################################################################





















