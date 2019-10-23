#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Defining a function and calling it

# func

#func():
    # Текст до инструкции return
    # Возвращаемое значение
    # print("Эта инструкция никогда не будет выполнена")

# print(_())

# print()
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

# print()
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

# print()
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

# print()
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

# print()
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

# ___ func x y
#     ___ i i_ r_ 1 x + 1
#         y_ i ** y
#
# i = f_ 3 3
# print(i.__n_  # Выведет: 1 (1 ** 3)
# print(i.__n_  # Выведет: 8 (2 ** 3)
# print(i.__n_  # Выведет: 27 (3 ** 3)
# print(i.__n_  # Исключение StopIteration
#
# print()
# ######################################################################################################################
#  Calling one generator function fro… (simple case)

# ___ gen l
#     ___ e __ l
#         y_ f_ r_ 1 e + 1
#
# l = [5, 10]
# ___ i __ g_([5, 10]): print i e_ - " ")
#
# print()
# ######################################################################################################################
# Calling one function generator fro…er (hard case)

# ___ gen2 n
#     ___ e __ r_ 1 n + 1
#         y_ e * 2
#
# ___ gen l
#     ___ e __ l
#         y_ f_ gen2(e)
#
# l = [5, 10]
# ___ i __ g_([5, 10]): print i e_ - " "
#
# print()
# ######################################################################################################################
# Specifying multiple decorators

# ___ deco1 f
#     print("Вызвана функция deco1()")
#     r_ f
# ___ deco2 f
#     print("Вызвана функция deco2()")
#     r_ f
# _deco1
# _deco2
# ___ func x
#     r_  x = _0_.f_ x
# print(f_(10))
#
# print()
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

# print()
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

# print()
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

# print()
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

# print()
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

# print()
# ######################################################################################################################
# Keywords

# ___ f a b c print a b c
#
# f(1, 2, 3)
# f(c=3, b=2, a=1)
# f(1, c=3, b=2)
#
# ___ f_(name='Bob', age=40, job='dev'): print(name, age, job)
#
# func('Serg,', 40, ', nuker')
#
# print()
# ######################################################################################################################
# Defaults

# ___ f a b_2 c_3): print a b c
#
# f(1)
# f(a=1)
# f(1, 4)
# f(1, 4, 5)
# f(1, c=6)
#
# print()
# ######################################################################################################################
# _combining keywords and defaults

# ___ func spam eggs toast_0 ham_0  # First 2 required
#     print spam eggs toast ham
#
# func(1, 2)  # Output: (1, 2, 0, 0)
# func(1, ham=1, eggs=0)  # Output: (1, 0, 0, 1)
# func(spam=1, eggs=0)  # Output: (1, 0, 0, 0)
# func(toast=1, eggs=2, spam=3)  # Output: (3, 2, 1, 0)
# func(1, 2, 3, 4)  # Output: (1, 2, 3, 4)

print()
# ######################################################################################################################
# Applying functions generically

# ___ func a b c d print a b c d
#
# args = (2, 3)
# args += (4, 5)
# print(args)
# f_(_args)
#
# ___ tracer func _pargs __kargs  # Accept arbitrary arguments
#     print 'calling:' f_.__n
#     r_ f_ _pargs __kargs  # Pass along arbitrary arguments
#
# ___ func a b c d
#     r_ a b c d
#
# # def func(a, b, c, d):
# #    return a + b + c + d
#
# print t_(f_ 1 2 c_3 d_4
#
# print()
# ######################################################################################################################
# Python 3.X Keyword-Only Arguments

# ___ kwonly a  _b c
#     print a b c
#
# kwonly 1 2 c_3
# kwonly a_1 c_3
#
# ___ kwonly a _ b c
#     print a b c
#
# kwonly 1 c_3 b_2
# kwonly(c_3 b_2 a_1
#
# ___ kwonly a _ b_ spam c_ ham
#     print a b c
#
# kwonly 1
# kwonly 1 c_3
# kwonly a_1
# kwonly c_3 b_2 a_1
#
# ___ kwonly a _ b c_ spam
#     print a b c
#
# kwonly 1 b_ eggs
#
# ___ kwonly a _ b_1 c d_2
#     print a b c d
#
# kwonly 3 c_4
# kwonly 3 c_4 b_5
#
# print()
# ######################################################################################################################
# Ordering rules
# Collect args in header

# ___ f a _b c_6 __d  print a b c d

# print()
# ######################################################################################################################
# Ordering rules
#  Default used

# ___ f a _b c_6 __d
# f 1 2 3 x_4 y_5

# print()
# ######################################################################################################################
# Ordering rules
#  Override default

# ___ f a _b c_6 __d
# f 1 2 3 x_4 y_5 c_7

# print()
# ######################################################################################################################
# Ordering rules
# Anywhere in keywords

# ___ f a _b c_6 __d
# f 1 2 3 c_7 x_4 y_5

# print()
# ######################################################################################################################
# Ordering rules
# c is not keyword-only

# ___ f a _b c_6 __d
# ___ f a c_6 _b __d print a b c d

# print()
# ######################################################################################################################
# Ordering rules
# KW-only between * and **

# ___ f a _b c_6 __d print a b c d

# print()
# ######################################################################################################################
# Ordering rules
# Unpack args at call

# ___ f a _b c_6 __d
# f 1 _(2 3) __d_ x_4 y_5

# print()
# ######################################################################################################################
# Ordering rules
# Override default

# ___ f a _b c_6 __d
# f 1 _(2, 3) c_7 __d_ x_4 y_5

# print()
# ######################################################################################################################
# Ordering rules
# After or before *

# ___ f a _b c_6 __d
# f 1 c_7 _(2, 3) __d_ x_4 y_5

# print()
# ######################################################################################################################
# Ordering rules
# Keyword-only in

# ___ f a _b c_6 __d
# f 1 _(2 3) __d_(x_4 y_5 c_7

# print()
# ######################################################################################################################
# Recursive Functions

# ___ mysum L
#     __ n_ L
#         r_ 0
#     e_
#         r_ L_0_ + m_(L_1___  # Call myself


# ___ m_
#     print m_([1 2 3 4 5]))

# print()
# ######################################################################################################################
# Recursive Functions

# ___ mysum
#     print L
#     __ n_ L
#         r_ 0
#     ___
#         r_ L_0_ + m_(L_1___  # Call myself

# ___ main
#     print m_([1, 2, 3, 4, 5]))

# print()
# ######################################################################################################################
# Recursive Functions

# ___ mysum
#     __ ___ L r__ 0
#     r_ nonempty 0  # Call a function that calls me

# ___ nonempty L
#     r_ L_0_ + mysum(L_1___  # Indirectly recursive

# ___ m_
#     print(m_([1.1, 2.2, 3.3, 4.4]))

# print()
# ######################################################################################################################
# Indirect Function Call

# ___ echo message  # Name echo assigned to function object
#     print message

# echo Direct call

# x  echo  # Now x references the function too
# x Indirect call!  # Call object through name by adding ()

# ___ indirect func arg
#     func arg  # Call the passed-in object by adding ()


# i_(e_ Argument call!  # Pass the function to another function

# print()
# ######################################################################################################################
# Functions can receive keyword arguments

# ___ has_keywords my_T_ name_ computer
#     __ my
#         print My name
#     ____
#         print Not mine name

# has_keywords name_ phone

# print()
# ######################################################################################################################
# Function can receive unlimited number of positional arguments

# ___ has_args _args
#     print A lot of arguments:  args

# has_args 1 demo [1, 2] (9 string))

# print()
# ######################################################################################################################
# Functions can receive unlimited number of keyword arguments

# ___ has_kwargs __kwargs
#     print A lot of keyword arguments kwargs
#     print kwargs is a dict t_(kwargs))

# has_kwargs any_possible_N_ values=[] you_wish_1

# print()
# ######################################################################################################################
# Function that will cover 100% of arguments

# ___ send_anything_args __kwargs
#     print args args
#     print kwargs kwargs

# send_anything 1 15 'a' value_T_ new_value_F_

# print()
# ######################################################################################################################
# Functions can use global variables

# GLOBAL_VAR = 3
#
# ___ using_global_var x
#     print x * G_
#
# using_global_var 12
#
# print()
# ######################################################################################################################
# Functions can use global variables
# But if we want to write to it, we should state it explicitly

# ___ writing_to_global_var value
#     g_ GLOBAL_VAR
#     G___ _ value
#     print it is now G_
#
# writing_to_global_var 9
#
# print()
# ######################################################################################################################
# Functions are objects and can be nested

# ___ outer_function value
#     ___ some_inner
#         print Value was  value

    # r_ s_

# v _ o_ some
# print _it is a function_  v c__v__
# v()  # 'some' will be printed

# print()
# ######################################################################################################################
#  map

# ___ work value
#     r_ value * 2

# t = [1, 2, 10]
# m _ m_ work t
# print m

# print()
# ######################################################################################################################
# map  but using lambda function

# m1 = m_|l_ x x * 2 t
# print(l_ m1

# print()
# ######################################################################################################################
# filter

# print(l_(f_(l_ v v > 0, [-1, -5, -9, 20, 3, 0])))

# print()
# ######################################################################################################################
# reduce

# f_ f_ i_ reduce

# r = [1, 4, 2, 3]
# result = r_(l x y x + y r
# print r_

# print()
# ######################################################################################################################
# functions_are_objects

# ___ my_function
#     print I am a function

# print Functions are objects_ i_ m_, o_

# print()
# ######################################################################################################################
# You can pass functions as parameters

# ___ call_passed_function incoming
#     print Calling!
#     i_()
#     print Called!

# call_passed_function my_function

# print()
# ######################################################################################################################
# You can check if something could be called

# print(c_(l_), c_ 45 c_(c_))

# print()
# ######################################################################################################################
# You can return function from a function

# ___ return_min_function
#     r_ min

# test = return_min_function__
# min_value = t_  4 5 -9 12
# print Min values is_  min_value

# print()
# ######################################################################################################################
#  Объявление функции hello_world

# Объявление функции hello_world
# ___ hello_world
#     print Hello, World!

# Вызов функции hello_world
# hello_world()

# print()
# ######################################################################################################################
# procedure-with-parameter

# limit - формальный параметр функции print_numbers
# ___ print_numbers limit
#     ___ i __ r_ limit
#         print i

# Здесь вызывается функция print_numbers, а её формальный
# параметр limit замещается фактическим параметром 10
# print_numbers 10

# print()
# ######################################################################################################################
# using-builtin-functions

# Функция из прошлого примера
# ___ print_numbers limit
#     ___ i __ r_ limit
#         print i

# Читаем ввод пользователя при помощи стандартной
# функции input, конструируем из него число при
# помощи стандартной функции int и записываем в
# переменную n
# n _ i_(i_ Введите n:
# Вызываем функцию print_numbers с фактическим параметром n
# print_numbers n

# print()
# ######################################################################################################################
# multiple-functions

# Функция из прошлого примера
# ___ print_numbers limit
#     __ i __ r_ limit
#         print i

# Любое логически завершённое действие следует помещать в функцию
# ___ main
#     n _ i_(i_ Введите n:
#     print_numbers _

# Вызов главной функции
# main()

# print()
# ######################################################################################################################
# main-function

# ___ main
#     print  Hello, World!

# Главную функцию желательно вызывать так
# (таким образом функция будет вызвана только если
# данный файл был запущен как главный; это важно
# для приложений, состоящих из нескольких модулей)
# __ __n_ __  __m_
#     m_

# print()
# ######################################################################################################################
# simple-function

# ___ add_numbers a b
#     r_ a + b  # возврат суммы параметров
#
#
# x _ add_numbers 2 3
# print(x)
#
# print()
# ######################################################################################################################
# procedures-as-functions

# ___ procedure
#     print I return nothing... Or I do?
#
# value = p_
# print Результат функции:_ value
#
# print()
# ######################################################################################################################
# multiple-return-statements

# Эта функция возвращает аргумент, умноженный на два,
# если он отрицательный, или аргумент, умноженный на три,
# если он больше или равен нулю
___ function(
    __ x < 0:
        r_ x * 2
    else:
        r_ x * 3


___ main():
    # Вывод значений функции в диапазоне [-3, 3]
    for i __ range(-3, 4):
        y = function(i)
        print('function(', i, ') = ', y, sep='')


__ __name__ == '__main__':
    main()

print()
# ######################################################################################################################
# return-in-procedures

___ hello(name):
    # Если имя пустое, выходим из функции
    __ not name:
        r_
    print('Hello, ', name, '!', sep='')


hello('Alex')
hello('')
hello('Python')

print()
# ######################################################################################################################
# functions-in-expressions

___ add(a, b):
    r_ a + b


___ sub(a, b):
    r_ a - b


# Вызов функции может быть частью выражения
print(add(2, 3) + sub(2, 3))  # => print((2 + 3) + (2 - 3))

print()
# ######################################################################################################################
# keyword-arguments

# Функция, которая принимает три аргумента
___ info(object, color, price):
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
___ hello name_'Alex'
    print 'Hello, ' name '!' s_-''

hello Python
hello()

print()
# ######################################################################################################################
# functions_as_first_class_objects

# Создание ссылки на объект
out = print
out Hello


# Сохранение ссылок на функции в структуре данных

___ add x y
    r_ x + y


___ sub(x, y):
    r_ x - y


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


___ make_closure():
    variable = 42

    ___ closure():
        r_ variable

    r_ closure


fn = make_closure()
print(fn())

print()
# ######################################################################################################################
# advanced_closure_example

"""Демонстрация часто допускаемой ошибки и способа её решения"""

___ make_powers(n):
    """Функция, возвращающая список функций, каждая из которых вычисляет
    степень аргумента, равную данному индексу плюс 1
    (неправильная реализация)
    """

    functions = []

    for i __ range(1, n + 1):
        functions.append(lambda x: x ** i)

    r_ functions


for function __ make_powers(3):
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

___ make_powers(n):
    """Функция, возвращающая список функций, каждая из которых вычисляет
    степень аргумента, равную данному индексу плюс 1"""

print()
# ######################################################################################################################
# Пример каррирования функции

___def ordinary_add(x, y):
    """Обычная функция"""
    return x + y


___ curryied_add(x):
    """Каррированная функция"""

    ___ do_add(y):
        r_ x + y

    r_ do_add

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

___ decorator(fn):
    """Пример декоратора"""

    ___ decorated_fn(*args, **kwargs):
        """Модифицированная функция"""

        print('Decorated function says:')
        fn(*args, **kwargs)  # вызов изначальной функции
        print()

    r_ decorated_fn


@decorator
___ hello():
    print('Hello!')


# Вызов декорированной функции
hello()

print()
# ######################################################################################################################
# Пример создания декоратора с параметром

___ cast_result(type_):
    """Пример создания декоратора с параметром"""

    ___ cast_decorator(function):
        """Сам декоратор"""

        ___ decorated_function(*args, **kwargs):
            result = function(*args, **kwargs)
            r_ type_(result)

        r_ decorated_function

    r_ cast_decorator

@cast_result(float)
___ add(x, y):
    r_ x + y

print(add(2, 3))

import decimal

@cast_result(repr)
@cast_result(decimal.Decimal)
___ div(x, y):
    r_ x / y


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
___ fibonacci(index):
    __ index < 2:
        r_ 1
    else:
        r_ fibonacci(index - 1) + fibonacci(index - 2)


for i __ range(1, 1000):
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

for a, b __ product(range(2), range(3)):
    print(a, b)

print()
# ######################################################################################################################
# Positional Arguments

# ___ my_func a b c
#     print "a_|0|_ b_|1|_ c_|2|".f_ a b c
# 
# print()
# ######################################################################################################################
# Default Values

# Note that once a parameter is assigned a default value, all parameters thereafter must be asigned a default value too!

# ___ my_func a b_2 c_3
#     print "a_|0}_ b_|1}_ c_|2|".f_ a b c
#
# my_func(10, 20, 30)
# my_func(10, 20)
# my_func(10)

# Since a does not have a default value, it must be specified:

# print()
# ######################################################################################################################
# Keyword Arguments (named arguments)

# ___ my_func a b_2 c_3
#     print "a_|0|_ b_|1}_ c_|2|".f_ a b c
#
# my_func c_30 b_20 a_10
# my_func 10 c_30 b_20

# Note that once a keyword argument has been used, all arguments thereafter must also be named:
#
# However, if a parameter has a default value, it can be omitted from the argument list, named or not:

# my_func 10 c_30
# my_func a_30 c_10
# my_func c_10, a_30
#
# print()
# ######################################################################################################################
#  arbitrary numbers of positional parameters/arguments:
#
# ___ func1 a b _args
#     print a
#     print b
#     print args
#
# func1 1 2 'a' 'b'

# A few things to note:
# Unlike iterable unpacking, *args will be a tuple, not a list.
# The name of the parameter args can be anything you prefer
# You cannot specify positional arguments after the *args parameter - this does something different that we'll cover in the next lecture.

# print()
# ######################################################################################################################
# how we might use this to calculate the average of an arbitrary number of parameters.

# ___ avg _args
#     count _ len_ args
#     total _ s_ args
#     r_ t_/c_
#
# avg 2 2 4 4
#
# avg() # error
#
# ___ avg _args
#     count _ l_ args
#     total _ s_ args
#     __ count __ 0
#         r_ 0
#     ___:
#         r_ t_/c_
#
# avg 2 2 4 4
# avg()

# But we may not want to allow specifying zero arguments, in which case we can split our parameters into a required (non-defaulted) positional argument, and the rest:

# ___ avg a _args
#     count _ l_(args) + 1
#     total _ a + s_ args
#     r_ t_/c_
#
# avg 2 2 4 4
# avg()
#
# print()
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
# *args **kwargs

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, a=100, b=200)

print()
# ######################################################################################################################
# If you want to specify both specific keyword-only arguments and **kwargs you will need to first get to a point
# where you can define a keyword-only argument (i.e. exhaust the positional arguments, using either *args or just *)

def func(*, d, **kwargs):
    print(d)
    print(kwargs)

func(d=1, x=100, y=200)

print()
# ######################################################################################################################
# Positionals Only: no extra positionals, no defaults (all positionals required)

def func(a, b):
    print(a, b)

func('hello', 'world')
func(b='world', a='hello')

print()
# ######################################################################################################################
# Positionals Only: no extra positionals, defaults (some positionals optional)

def func(a, b='world', c=10):
    print(a, b, c)

func('hello')
func('hello', c='!')

print()
# ######################################################################################################################
# Positionals Only: extra positionals, no defaults (all positionals required)

def func(a, b, *args):
    print(a, b, args)

func(1, 2, 'x', 'y', 'z')

print()
# ######################################################################################################################
# Keywords Only: no positionals, no defaults (all keyword args required)

def func(*, a, b):
    print(a, b)

func(a=1, b=2)

print()
# ######################################################################################################################
# Keywords Only: no positionals, some defaults (not all keyword args required)

def func(*, a=1, b):
    print(a, b)

func(a=10, b=20)
func(b=2)

print()
# ######################################################################################################################
# Keywords and Positionals: some positionals (no defaults), keywords (no defaults)

def func(a, b, *, c, d):
    print(a, b, c, d)

func(1, 2, c=3, d=4)
func(1, 2, d=4, c=3)
func(1, c=3, d=4, b=2)

print()
# ######################################################################################################################
# Keywords and Positionals: some positional defaults

def func(a, b=2, *, c, d=4):
    print(a, b, c, d)

func(1, c=3)
func(c=3, a=1)
func(1, 2, c=3, d=4)
func(c=3, a=1, b=2, d=4)

print()
# ######################################################################################################################
# Keywords and Positionals: extra positionals

def func(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)

func(1, 2, 'x', 'y', 'z', c=3, d=4)

Note that if we are going to use the extra arguments, then we cannot actually use a default value for b:

func(1, 'x', 'y', 'z', c=3, d=4)

print()
# ######################################################################################################################
# Keywords and Positionals: no extra positionals, extra keywords

def func(a, b, *, c, d=4, **kwargs):
    print(a, b, c, d, kwargs)

func(1, 2, c=3, x=100, y=200, z=300)
func(x=100, y=200, z=300, c=3, b=2, a=1)

print()
# ######################################################################################################################
# Keywords and Positionals: extra positionals, extra keywords

def func(a, b, *args, c, d=4, **kwargs):
    print(a, b, args, c, d, kwargs)

func(1, 2, 'x', 'y', 'z', c=3, d=5, x=100, y=200, z=300)

print()
# ######################################################################################################################
# Keywords and Positionals: only extra positionals and extra keywords

def func(*args, **kwargs):
    print(args, kwargs)

func(1, 2, 3, x=100, y=200, z=300)

print()
# ######################################################################################################################
# Another Use Case
# log_to_console

def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo)/2
    if log_to_console:
        print("high={0}, low={1}, avg={2}".format(hi, lo, avg))
    return avg

avg = calc_hi_lo_avg(1, 2, 3, 4, 5)
print(avg)

avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=True)
print(avg)

print()
# ######################################################################################################################
# A Simple Function Timer

import time

def time_it(fn, *args, rep=5, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep


def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]

def compute_powers_3(n, *, start=1, end):
    # using a generator expression
    return (n**i for i in range(start, end))

compute_powers_1(2, end=5)
compute_powers_2(2, end=5)
list(compute_powers_3(2, end=5))

time_it(compute_powers_1, n=2, end=20000, rep=4)
time_it(compute_powers_2, 2, end=20000, rep=4)
time_it(compute_powers_3, 2, end=20000, rep=4)

print()
# ######################################################################################################################
# We can define such help using docstrings

def my_func(a, b):
    'Returns the product of a and b'
    return a*b

help(my_func)

print()
# ######################################################################################################################
# Docstrings can span multiple lines using a multi-line string literal:


def fact(n):
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n - 1)


help(fact)

Docstrings, when
found, are
simply
attached
to
the
function in the
__doc__
property:


fact.__doc__

print()
# ######################################################################################################################
# Annotations

def my_func(a: 'annotation for a',
            b: 'annotation for b') -> 'annotation for return':
    return a * b


help(my_func)

print()
# ######################################################################################################################
# The annotations can be any expression, not just strings:

x = 3
y = 5
def my_func(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
	return a*max(x, y)

help(my_func)

print()
# ######################################################################################################################
# Just like docstrings are stored in the __doc__ property, annotations are stored in the __annotations__ property -
# a dictionary whose keys are the parameter names, and values are the annotation.

x = 3
y = 5
def my_func(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
	return a*max(x, y)

my_func.__annotations__

print()
# ######################################################################################################################
# Annotations will work with default parameters too: just specify the default after the annotation

def my_func(a:str='a', b:int=1)->str:
    return a*b

help(my_func)
my_func()
my_func('abc', 3)

def my_func(a:int=0, *args:'additional args'):
    print(a, args)

my_func.__annotations__

help(my_func)

print()
# ######################################################################################################################
# Lambda Expressions

lambda x: x**2

print()
# ######################################################################################################################
# Lambda Assigning to a Variable

func = lambda x: x**2

type(func)
func(3)

print()
# ######################################################################################################################
# We can specify arguments for lambdas just like we would for any function created using def, except for annotations:

func_1 = lambda x, y=10: (x, y)
func_1(1, 2)
func_1(1)

print()
# ######################################################################################################################
# Lambda We can even use * and **:

func_2 = lambda x, *args, y, **kwargs: (x, *args, y, {**kwargs})

func_2(1, 'a', 'b', y=100, a=10, b=20)

print()
# ######################################################################################################################
# Lambda
# Passing as an Argument
# Lambdas are functions, and can therefore be passed to any other function as an argument
# (or returned from another function)

def apply_func(x, fn):
    return fn(x)
apply_func(3, lambda x: x**2)
apply_func(3, lambda x: x**3)

print()
# ######################################################################################################################
# Lambda
# Passing as an Argument
# Lambdas are functions, and can therefore be passed to any other function as an argument
# (or returned from another function)
# we can make this even more generic:

def apply_func(fn, *args, **kwargs):
    return fn(*args, **kwargs)

apply_func(lambda x, y: x+y, 1, 2)
apply_func(lambda x, *, y: x+y, 1, y=2)
apply_func(lambda *args: sum(args), 1, 2, 3, 4, 5)

print()
# ######################################################################################################################
# Lambdas and Sorting

l = ['a', 'B', 'c', 'D']
sorted(l)
sorted(l, key=str.upper)

We could have used a lambda here (but you should not, this is just to illustrate using a lambda in this case):

sorted(l, key = lambda s: s.upper())

print()
# ######################################################################################################################
# Lambdas and Sorting
# Let's look at how we might create a sorted list from a dictionary:

d = {'def': 300, 'abc': 200, 'ghi': 100}
d
sorted(d)

sorted(d, key=lambda k: d[k])

print()
# ######################################################################################################################
#  here's another example where we want to sort a list of strings based on the last character of the string:

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']

sorted(l)

sorted(l, key=lambda s: s[-1])

print()
# ######################################################################################################################
# Randomizing an Iterable using Sorted

import random
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted(l, key=lambda x: random.random())
sorted('abcdefg', key = lambda x: random.random())

And to get a string back instead of just a list:

''.join(sorted('abcdefg', key = lambda x: random.random()))

print()
# ######################################################################################################################
# Function Introspection
# The name attribute holds the function's name:

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func


my_func.__name__
f.__name__

print()
# ######################################################################################################################
# Function Introspection
# The defaults attribute is a tuple containing any positional parameter defaults:

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass
f = my_func

my_func.__defaults__
my_func.__kwdefaults__

print()
# ######################################################################################################################
# Function Introspection
# The code attribute contains a code object:

def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

my_func('a', 100)

my_func.__code__

dir(my_func.__code__)

print()
# ######################################################################################################################
# Function Introspection
#
# Attribute co_varnames is a tuple containing the parameter names and local variables:

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func

my_func.__code__.co_varnames

print()
# ######################################################################################################################
# Function Introspection
# Attribute co_argcount returns the number of arguments (minus any * and ** args)

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func
my_func.__code__.co_argcount

print()
# ######################################################################################################################
# The inspect module

def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

my_func('a', 100)

import inspect
inspect.isfunction(my_func)
inspect.ismethod(my_func)

print()
# ######################################################################################################################
# Introspecting Callable Code

def fact(n: "some non-negative integer") -> "n! or 0 if n < 0": """Calculates the factorial of a non-negative integer n

If n is negative, returns 0.
"""
if n < 0:
    return 0
elif n <= 1:
    return 1
else:
    return n * fact(n-1)

inspect.getsource(fact)

print()
# ######################################################################################################################
# Functions and Methods are callable

callable(print)
callable(len)
l = [1, 2, 3]
callable(l.append)
s = 'abc'
callable(s.upper)

print()
# ######################################################################################################################
# Callables always return a value:

result = print('hello')
print(result)

l = [1, 2, 3]
result = l.append(4)
print(result)
print(l)

s = 'abc'
result = s.upper()
print(result)

print()
# ######################################################################################################################
# Classes are callable:

from decimal import Decimal
callable(Decimal)
result = Decimal('10.5')
print(result)

print()
# ######################################################################################################################
# Class instances may be callable:

class MyClass:
    def __init__(self):
        print('initializing...')
        self.counter = 0

    def __call__(self, x=1):
        self.counter += x
        print(self.counter)


my_obj = MyClass()
callable(my_obj.__init__)
callable(my_obj.__call__)
my_obj()
my_obj()
my_obj(10)

print()
# ######################################################################################################################
# Map

The map built-in function is a higher-order function that applies a function to an iterable type object:

def fact(n):
    return 1 if n < 2 else n * fact(n-1)

fact(3)
fact(4)

map(fact, [1, 2, 3, 4, 5])

The map function returns a map object, which is an iterable - we can either convert that to a list or enumerate it:

l = list(map(fact, [1, 2, 3, 4, 5]))
print(l)

We can also use it this way:

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

f = lambda x, y: x+y

m = map(f, l1, l2)
list(m)

print()
# ######################################################################################################################
# Filter

The filter function is a function that filters an iterable based on the truthyness of the elements, or the truthyness of the elements after applying a function to them. Like the map function, the filter function returns an iterable that we can view by generating a list from it, or simply enumerating in a for loop.

l = [0, 1, 2, 3, 4, 5, 6]
for e in filter(None, l):
    print(e)

print()
# ######################################################################################################################
# is_even with filter

def is_even(n):
    return n % 2 == 0

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(is_even, l)
print(list(result))

Of course, we could just use a lambda expression instead:

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, l)
print(list(result))

print()
# ######################################################################################################################
# Map using a list comprehension

l = [1, 2, 3, 4, 5]
result = [fact(i) for i in l]
print(result)

print()
# ######################################################################################################################
# The zip built-in function will take one or more iterables,
# and generate an iterable of tuples where each tuple contains one element from each iterable:

l1 = 1, 2, 3
l2 = 'a', 'b', 'c'
list(zip(l1, l2))

l1 = 1, 2, 3
l2 = [10, 20, 30]
l3 = ('a', 'b', 'c')
list(zip(l1, l2, l3))

l1 = [1, 2, 3]
l2 = (10, 20, 30)
l3 = 'abc'
list(zip(l1, l2, l3))

l1 = range(100)
l2 = 'python'
list(zip(l1, l2))

print()
# ######################################################################################################################
# Using the zip function we can now add our two lists element by element as follows:

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
result = [i + j for i,j in zip(l1,l2)]
print(result)

print()
# ######################################################################################################################
# Filtering using a comprehension

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [i for i in l if i % 2 == 0]
print(result)

print()
# ######################################################################################################################
# Combining map and filter

list(filter(lambda y: y < 25, map(lambda x: x**2, range(10))))

# Alternatively, we can use a list comprehension to do the same thing:

[x**2 for x in range(10) if x**2 < 25]

print()
# ######################################################################################################################
# Suppose we want to find the maximum value in a list:
#
# First we define a function that returns the maximum of two arguments:

l = [5, 8, 6, 10, 9]

_max = lambda a, b: a if a > b else b

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

max_sequence(l)

print()
# ######################################################################################################################
# To calculate the minimum, all we need to do is to change the function that is repeatedly applied

l = [5, 8, 6, 10, 9]

_min = lambda a, b: a if a < b else b

def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result

print(l)
print(min_sequence(l))

print()
# ######################################################################################################################
# Maximum and Minimum
# Using Reducing Functions

l = [5, 8, 6, 10, 9]
_max = lambda a, b: a if a > b else b
_min = lambda a, b: a if a < b else b

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

_reduce(_max, l)
_reduce(_min, l)

We could even just use a lambda directly in the call to _reduce:

_reduce(lambda a, b: a if a > b else b, l)
_reduce(lambda a, b: a if a < b else b, l)

print()
# ######################################################################################################################
# Python actually implements a reduce function, which is found in the functools module.
# Unlike our _reduce function, it can handle any iterable, not just sequences.

from functools import reduce
l = [5, 8, 6, 10, 9]
l
reduce(lambda a, b: a if a > b else b, l)
reduce(lambda a, b: a if a < b else b, l)
reduce(lambda a, b: a if a < b else b, l)
reduce(lambda a, b: a + b, l)

print()
# ######################################################################################################################
# Finding the max and min of an iterable is such a common thing that Python provides a built-in function to do just that:

l = [5, 8, 6, 10, 9]
max(l), min(l)
sum(l)

print()
# ######################################################################################################################
# The any and all built-ins

l = [0, 1, 2]
any(l)

l = [0, 0, 0]
any(l)

print()
# ######################################################################################################################
# On the other hand, all will return True if every element of the iterable is truthy:

l = [0, 1, 2]
all(l)

l = [1, 2, 3]
all(l)

print()
# ######################################################################################################################
# We can implement any functions ourselves using reduce if we choose to - simply use the Boolean or or and operators as
# the function passed to reduce to implement any and all respectively.

l = [0, 1, 2]
reduce(lambda a, b: bool(a or b), l)

l = [0, 0, 0]
reduce(lambda a, b: bool(a or b), l)

print()
# ######################################################################################################################
# We can implement all functions ourselves using reduce if we choose to - simply use the Boolean or or and operators as
# the function passed to reduce to implement any and all respectively.

l = [0, 1, 2]
reduce(lambda a, b: bool(a and b), l)

l = [1, 2, 3]
reduce(lambda a, b: bool(a and b), l)

print()
# ######################################################################################################################
# Partial Functions

from functools import partial
def my_func(a, b, c):
    print(a, b, c)
f = partial(my_func, 10)
f(20, 30)

We could have done this using another function (or a lambda) as well:

def partial_func(b, c):
    return my_func(10, b, c)

or, using a lambda:

fn = lambda b, c: my_func(10, b, c)
fn(20, 30)

print()
# ######################################################################################################################
# Partial Functions
# it is quite flexible with parameters:

def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

f = partial(my_func, 10, k1='a')
f(20, 30, 40, k2='b', k3='c')

We can of course do the same thing using a regular function too:

def f(b, *args, k2, **kwargs):
    return my_func(10, b, *args, k1='a', k2=k2, **kwargs)

f(20, 30, 40, k2='b', k3='c')

print()
# ######################################################################################################################
# Partial Functions
# you are not stuck having to specify the first argument in your partial:

def power(base, exponent):
    return base ** exponent

power(2, 3)
square = partial(power, exponent=2)
square(4)
cube = partial(power, exponent=3)
cube(2)

cube(base=3)

print()
# ######################################################################################################################
# suppose we have points (represented as tuples), and we want to sort them based on the distance of the point from
# some other fixed point:

origin = (0, 0)
l = [(1,1), (0, 2), (-3, 2), (0,0), (10, 10)]
dist2 = lambda x, y: (x[0]-y[0])**2 + (x[1]-y[1])**2
dist2((0,0), (1,1))
sorted(l, key = lambda x: dist2((0,0), x))
sorted(l, key=partial(dist2, (0,0)))

print()
# ######################################################################################################################
#  we have some generic email() function that can be used to notify someone when various things happen
#  in our application. But depending on what is happening we may want to notify different people.

def sendmail(to, subject, body):
    # code to send email
    print('To:{0}, Subject:{1}, Body:{2}'.format(to, subject, body))

Now, we may haver different email adresses we want to send notifications to, maybe defined in a config file in our app. Here, I'll just use hardcoded variables:

email_admin = 'palin@python.edu'
email_devteam = 'idle@python.edu;cleese@python.edu'

Now when we want to send emails we would have to write things like:

sendmail(email_admin, 'My App Notification', 'the parrot is dead.')
sendmail(';'.join((email_admin, email_devteam)), 'My App Notification', 'the ministry is closed until further notice.')

We could simply our life a little using partials this way:

send_admin = partial(sendmail, email_admin, 'For you eyes only')
send_dev = partial(sendmail, email_devteam, 'Dear IT:')
send_all = partial(sendmail, ';'.join((email_admin, email_devteam)), 'Loyal Subjects')

send_admin('the parrot is dead.')
send_all('the ministry is closed until further notice.')

Finally, let's make this a little more complex, with a mixture of positional and keyword-only argument

print()
# ######################################################################################################################
# Functions defined inside anther function can reference variables from that enclosing scope,
# just like functions can reference variables from the global scope.

def outer_func():
    x = 'hello'

    def inner_func():
        print(x)

    inner_func()


outer_func()

print()
# ######################################################################################################################
# if we assign a value to a variable, it is considered part of the local scope, and potentially masks enclsogin scope
# variable names:

x = 'hello'
def inner():
    nonlocal x
    x = 'python'
inner()
print(x)

outer()

# Of course, this can work at any level as well:

def outer():
    x = 'hello'

    def inner1():
        def inner2():
            nonlocal
            x
            x = 'python'

        inner2()

    inner1()
    print(x)


outer()

print()
# ######################################################################################################################
# Let's examine that concept of a cell to create an indirect reference for variables that are in multiple scopes.

def outer():
    x = 'python'
    def inner():
        print(x)
    return inner

fn = outer()
fn.__code__.co_freevars
fn.__closure__

print()
# ######################################################################################################################
# Modifying the Free Variable
# We know we can modify nonlocal variables by using the nonlocal keyword. So the following will work:

def counter():
    count = 0  # local variable

    def inc():
        nonlocal
        count  # this is the count variable in counter
        count += 1
        return count

    return inc


c = counter()
c()
c()

print()
# ######################################################################################################################
# Shared Extended Scopes

def outer():
    count = 0

    def inc1():
        nonlocal
        count
        count += 1
        return count

    def inc2():
        nonlocal
        count
        count += 1
        return count

    return inc1, inc2


fn1, fn2 = outer()
fn1.__closure__, fn2.__closure__

# As you can see here, the count label points to the same cell.

fn1()
fn1()
fn2()

print()
# ######################################################################################################################
# Multiple Instances of Closures
# Recall that every time a function is called, a new local scope is created.

from time import perf_counter

def func():
    x = perf_counter()
    print(x, id(x))

func()
func()

print()
# ######################################################################################################################
# Multiple Instances of Closures
# The same thing happens with closures, they have their own extended scope every time the closure is created:

def pow(n):
    # n is local to pow
    def inner(x):
        # x is local to inner
        return x ** n
    return inner

In this example, n, in the function inner is a free variable, so we have a closure that contains inner and the free variable n

square = pow(2)
square(5)
cube = pow(3)
cube(5)

We can see that the cell used for the free variable in both cases is different:

square.__closure__
cube.__closure__

print()
# ######################################################################################################################
# we wrote a simple closure to count how many times a function had been run:

def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal
        count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner


def add(a, b=0):
    """
    returns the sum of a and b
    """
    return a + b


add = counter(add)
add(1, 2)
add(2, 2)

print()
# ######################################################################################################################
# call that counter function a decorator.

def counter(fn):
    count = 0

    def inner(*args, **kwargs):
        nonlocal
        count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner


@counter
def mult(a: float, b: float = 1, c: float = 1) -> float:
    """
    returns the product of a, b, and c
    """
    return a * b * c


mult(1, 2, 3)
mult(2, 2, 2)

Let
's do a little bit of introspection on our two decorated functions:

add.__name__
mult.__name__

print()
# ######################################################################################################################
# We can use a special function in the functools module, called wraps. In fact, that function is a decorator itself!

from functools import wraps


def counter(fn):
    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal
        count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))

    return inner


@counter
def add(a: int, b: int = 10) -> int:
    """
    returns sum of two integers
    """
    return a + b


inspect.getsource(add)
inspect.signature(add)
inspect.signature(add).parameters

print()
# ######################################################################################################################
# Simulating a simple Switch in Python

def dow_switch_fn(dow):
    if dow == 1:
        fn = lambda: print('Monday')
    elif dow == 2:
        fn = lambda: print('Tuesday')
    elif dow == 3:
        fn = lambda: print('Wednesday')
    elif dow == 4:
        fn = lambda: print('Thursday')
    elif dow == 5:
        fn = lambda: print('Friday')
    elif dow == 6:
        fn = lambda: print('Saturday')
    elif dow == 7:
        fn = lambda: print('Sunday')
    else:
        fn = lambda: print('Invalid day of week')

    return fn()


dow_switch_fn(1)
dow_switch_fn(100)

print()
# ######################################################################################################################
# Simulating a simple Switch in Python
# dictionaries could also be used quite effectively here:

def dow_switch_dict(dow):
    dow_dict = {
        1: lambda: print('Monday'),
        2: lambda: print('Tuesday'),
        3: lambda: print('Wednesday'),
        4: lambda: print('Thursday'),
        5: lambda: print('Friday'),
        6: lambda: print('Saturday'),
        7: lambda: print('Sunday'),
        'default': lambda: print('Invalid day of week')
    }

    return dow_dict.get(dow, dow_dict['default'])()


dow_switch_dict(1)
dow_switch_dict(100)

print()
# ######################################################################################################################
# Simulating a simple Switch in Python
# recall our own implementation of the @singledispatch decorator:

def switcher(fn):
    registry = dict()
    registry['default'] = fn

    def register(case):
        def inner(fn):
            registry[case] = fn
            return fn  # we do this so we can stack register decorators!

        return inner

    def decorator(case):
        fn = registry.get(case, registry['default'])
        return fn()

    decorator.register = register
    return decorator


@switcher
def dow():
    print('Invalid day of week')


@dow.register(1)
def dow_1():
    print('Monday')


dow.register(2)(lambda: print('Tuesday'))
dow.register(3)(lambda: print('Wednesday'))
dow.register(4)(lambda: print('Thursday'))
dow.register(5)(lambda: print('Friday'))
dow.register(6)(lambda: print('Saturday'))
dow.register(7)(lambda: print('Sunday'))

dow(1)
dow(2)
dow(100)

print()
# ######################################################################################################################
# Introduction to Decorators
# be_polite

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper


def greet():
    print("My name is Colt.")


def rage():
    print("I HATE YOU!")

# we are decorating our function
# with politeness!


greet = be_polite(greet)

polite_rage = be_polite(rage)
polite_rage()

print()
# ######################################################################################################################
# Introduction to Decorators_decorate-syntax - be polite

def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper


@be_polite
def greet():
    print("My name is Colt.")


@be_polite
def rage():
    print("I HATE YOU!")


greet()
rage()

print()
# ######################################################################################################################
#  Decorators With Different Signatures
# shout example

ef shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    return f"Hi, I'm {name}."


@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."


@shout
def lol():
    return "lol"


print(greet("todd"))
print(order(side="burger", main="fries"))
print(lol())

print()
# ######################################################################################################################
# Using Wraps To Preserve Metadata

from functools import wraps


def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x, y):
    """Adds two numbers together."""
    return x + y


print(add.__doc__)
print(add.__name__)
help(add)

print()
# ######################################################################################################################
# Building A Speed-Test Decorator

from functools import wraps
from time import time


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_gen():
    return sum(x for x in range(90000000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(90000000)])


print(sum_nums_gen())
print(sum_nums_list())

print()
# ######################################################################################################################
# Another Example Ensuring Args With A Decorator
from functools import wraps


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if kwargs:
            raise ValueError("No kwargs allowed! sorry :(")
        return fn(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    print(f"hi there {name}")


greet(name="Tony")

print()
# ######################################################################################################################
# 290. Writing an ensure_first_arg_is Decorator_ensure-first-arg

from functools import wraps


def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args, **kwargs)
        return wrapper
    return inner


@ensure_first_arg_is("burrito")
def fav_foods(*foods):
    print(foods)


print(fav_foods("burrito", "ice cream")) # ('burrito', 'ice cream')
print(fav_foods("ice cream", "burrito")) # 'Invalid! First argument must be burrito'


@ensure_first_arg_is(10)
def add_to_ten(num1, num2):
    return num1 + num2


print(add_to_ten(10, 12))  # 12
print(add_to_ten(1, 2))  # 'Invalid! First argument must be 10'

print()
# ######################################################################################################################
# Enforcing Argument Types With A Decorator

def enforce(*types):
    def decorator(f):
        def new_func(*args, **kwargs):
            # convert args into something mutable
            newargs = []
            for (a, t) in zip(args, types):
               newargs.append( t(a))  # feel free to have more elaborated convertion
            return f(*newargs, **kwargs)
        return new_func
    return decorator


@enforce(str, int)
def repeat_msg(msg, times):
    for time in range(times):
        print(msg)


@enforce(float, float)
def divide(a, b):
    print(a/b)
# repeat_msg("hello", '5')


divide('1', '4')

print()
# ######################################################################################################################
# Using a @syntax
# user_has_permission

user = {'username': 'jose123', 'access_level': 'guest'}


def user_has_permission(func):
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func


@user_has_permission
def my_function():
    """
    Allows us to retrieve the password for the admin panel.
    """
    return 'Password for admin panel is 1234.'


@user_has_permission
def another():
    pass


print(my_function.__name__)
print(another.__name__)

print()
# ######################################################################################################################
# Functools wraps in Python
# user_has_permission

import functools

user = {'username': 'jose123', 'access_level': 'guest'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func():
        if user.get('access_level') == 'admin':
            return func()
    return secure_func


@user_has_permission
def my_function():
    """
    Allows us to retrieve the password for the admin panel.
    """
    return 'Password for admin panel is 1234.'


@user_has_permission
def another():
    pass


print(my_function.__name__)
print(another.__name__)

print()
# ######################################################################################################################
# Decorating functions with parameters
# user_has_permission

import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(panel):
        if user.get('access_level') == 'admin':
            return func(panel)
    return secure_func


@user_has_permission
def my_function(panel):
    """
    Allows us to retrieve the password for the admin panel.
    """
    return f'Password for {panel} panel is 1234.'


print(my_function.__name__)

print(my_function('movies'))

print()
# ######################################################################################################################
# Decorators with parameters
# user_has_permission

import functools

user = {'username': 'jose123', 'access_level': 'user'}


def user_has_permission(access_level):
    def my_decorator(func):
        @functools.wraps(func)
        def secure_func(panel):
            if user.get('access_level') == access_level:
                return func(panel)
        return secure_func
    return my_decorator


@user_has_permission('user')
def my_function(panel):
    """
    Allows us to retrieve the password for the admin panel.
    """
    return f'Password for {panel} panel is 1234.'


print(my_function.__name__)
print(my_function('movies'))

print()
# ######################################################################################################################
#  Generic decorators for any function
# user_has_permission

import functools

user = {'username': 'jose123', 'access_level': 'admin'}


def user_has_permission(func):
    @functools.wraps(func)
    def secure_func(*args, **kwargs):
        if user.get('access_level') == 'admin':
            return func(*args, **kwargs)
    return secure_func


@user_has_permission
def my_function(panel):
    """
    Allows us to retrieve the password for the admin panel.
    """
    return f'Password for {panel} panel is 1234.'


@user_has_permission
def another():
    pass


print(my_function.__name__)

print(my_function('movies'))
print(another())

print()
# ######################################################################################################################
# Пример работы с функциями как с объектами первого класса
"""Пример работы с функциями как с объектами первого класса"""

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
# Пример использования лямбда-выражений

operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y
}

print(operations['+'](2, 3))
print(operations['-'](2, 3))

print()
# ######################################################################################################################
# Пример замыкания

def make_closure():
    variable = 42

    def closure():
        return variable

    return closure


fn = make_closure()
print(fn())

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

# Пример использования функций takewhile и dropwhile модуля itertools

from itertools import takewhile, dropwhile


numbers = [1, 4, 6, 4, 1]
predicate = lambda x: x < 5

for value in takewhile(predicate, numbers):
    print(value)

print()

for value in dropwhile(predicate, numbers):
    print(value)

print()
# ######################################################################################################################
# Пример использования модуля operator

from operator import neg, mul, le
from functools import reduce, partial

# Сделать числа списка отрицательными
print(list(map(neg, [2, 4, 8, 9, 1])))

# Вычислить произведение элементов списка
print(reduce(mul, [3, 4, 5]))

# Оставить только числа, большие или равные пяти (используется оператор <=, так
# как при помощи функции partial применяется первый аргумент, то есть условие
# выглядит как 5 <= x).
print(list(filter(partial(le, 5), [5, 4, 8, 1, 3, 10])))

print()
# ######################################################################################################################





















