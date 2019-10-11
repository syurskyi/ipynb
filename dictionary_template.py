#!/usr/bin/python
# -*- coding: utf-8 -*-

# Создаем пустой словарь
# 2 options

# ######################################################################################################################
# Создать словарь можно следующими способами:
# Создать Словарь
# diсt(<Ключ1>=<Значение1>[, ... , <КлючN>=<ЗначениеN>])
# d
# print(_)
print()
# ######################################################################################################################
# Создать  Список кортежей
# d
# print(_)
print()
# ######################################################################################################################
# Создать Список списков
# d
# print(_)
print()
# ######################################################################################################################
# Объединить два списка в список кортежей позволяет функция zip()
k = ["a", "b"]  # Список с ключами
v = [1, 2]  # Список со значениями
# print(_(_(_,_)))     # # # # Создание списка кортежей zip
# d                    # # # # Создание словаря
# print(_)
print()
# ######################################################################################################################
# заполнив словарь поэлементно
# # # # Создаем пустой словарь
# d
# # # # Добавляем элемент1

# # # # Добавляем элемент2

# print(_)
print()
# ######################################################################################################################
# dict. fromkeys ( <Последовательность> [, <Значение>])
# d (a b c)
# print(_)
# d (a b c)   # Указан список
# print(_)
# d (a b c)   # Указан кортеж
# print(_)

print()
# ######################################################################################################################
# Creating a shallow copy of the dictionary using the dict () function
d1 = {"a": 1, "b": 2}  # Создаем словарь
# # # # Создаем поверхностную копию
# d2
# # # # Оператор показывает, что это разные объекты
# print(_ _)
# 10
# # # # Изменилось только значение в переменной d2
# print(_, _)

print()
# ######################################################################################################################
# Creating a shallow copy of the dictionary using the copy () method
d1 = {"a": 1, "b": 2}  # Создаем словарь
# # # # Создаем поверхностную копию
# d2
# # # # Оператор показывает, что это разные объекты
# print(_ _)
# 10
# # # # Изменилось только значение в переменной d2
# print(_,_)

print()
# ######################################################################################################################
# Creating a complete copy of the dictionary
d1 = {"a": 1, "b": [20, 30, 40]}
# import
# # # # # Создаем полную копию
# d3
# 800
# # # # # Изменилось значение только в переменной d3
# print(_, _)

print()
# ######################################################################################################################
# Выведем все элементы словаря:
d = {1: "int", "a": "str", (1, 2): "tuple"}
print(__, ___, ____)

print()
# ######################################################################################################################
# Если элемент, соответствующий указанному ключу, отсутствует в словаре, то возбуждается
# исключение KeyError:
d = {"a": 1, "b": 2}
# print(__)

print()
# ######################################################################################################################
# Проверить существование кточа можно с помощью оператора in. Если ключ найден, то
# возвращается значение тrue, в противном случае - False.
d = {"a": 1, "b": 2}
# print(_ _ _)      # Ключ существует
# print(_ _ _)      # Ключ не существует

print()
# ######################################################################################################################
# Проверить, отсутствует ли какой-либо ключ в словаре, позволит оператор not in. Если
# ключ отсутствует, возвращается True, иначе - False.
d = {"a": 1, "b": 2}
# print(_ _ _)    # Ключ не существует
# print(_ _ _)    # Ключ существует

print()
# ######################################################################################################################
# get ( <Ключ> [, <Значение по умолчанию> ] )
d = {"a": 1, "b": 2}
# print(_._(_), _._(_), _._(_, _))

print()
# ######################################################################################################################
# setdefault ( <Kлюч> [, <Значение по умолчанию>])
d = {"a": 1, "b": 2}
# print(_._(_), _._(_), _._(_,_))

print()
# ######################################################################################################################
# Изменение элемента по ключу
d = {"a": 1, "b": 2}
# # # # Изменение элемента по ключу
# 800
# # # # Будет добавлен новый элемент
# string
# print(_)

print()
# ######################################################################################################################
# len()
d = {"a": 1, "b": 2}
# print(_)    # Получаем количество ключей в словаре

print()
# ######################################################################################################################
# del()
d = {"a": 1, "b": 2}
# ______; print(_) # Удаляем элемент с ключом "b" и выводим словарь

print()
# ######################################################################################################################
# Perebor elementov slovarja
# 2 versions
d = {"x": 1, "y": 2, "z": 3}
# key
# print({} => {}).__(_,_[_]), _=_)

# key
# print({} => {}).__(_,_[_]), _=_)

print()
# ######################################################################################################################
# Получаем список ключей
d = {"x": 1, "y": 2, "z": 3}
# # # # Получаем список ключей
# k
# # # # Сортируем список ключей
# _._()
# key
# print({} => {}).__(_,_[_]), _=_)

print()
# ######################################################################################################################
#  sorted ( )
d = {"x": 1, "y": 2, "z": 3}
# key
# print({} => {}).__(_,_[_]), _=_)

# Так как на каждой итерации возвращается кmоч словаря, функции sorted ( ) можно сразу передать объект словаря,
# а не результат выполнения метода keys () :
d = {"x": 1, "y": 2, "z": 3}
# key
# print({} => {}).__(_,_[_]), _=_)

print()
# ######################################################################################################################
# Методы  для работы со словарями
# keys ()
d1, d2 = {"a": 1, "b": 2}, {"a": 3, "c": 4, "d": 5}
# # # # Получаем объект dict_keys
# print(_._, _._)
# # # # Получаем список ключей
# print(_(_._), _(_._))
# k

print()
# ######################################################################################################################
# Методы  для работы со словарями
# keys () - Объединение
d1, d2 = {"a": 1, "b": 2}, {"a": 3, "c": 4, "d": 5}
# print(_._ _._)

print()
# ######################################################################################################################
# Методы  для работы со словарями
# keys () - Разница
d1, d2 = {"a": 1, "b": 2}, {"a": 3, "c": 4, "d": 5}
# print(_._ _._)
# print(_._ _._)

print()
# ######################################################################################################################
# Методы  для работы со словарями
# keys () - Одинаковые ключи
d1, d2 = {"a": 1, "b": 2}, {"a": 3, "c": 4, "d": 5}
# print(_._ _._)

print()
# ######################################################################################################################
# Методы  для работы со словарями
# keys () - Уникальные ключи
d1, d2 = {"a": 1, "b": 2}, {"a": 3, "c": 4, "d": 5}
# print(_._ _._)

print()
# ######################################################################################################################
# Методы  для работы со словарями
# values ()
d = {"a": 1, "b": 2}
# # # # Получаем объект
# print(_._)
# # # # Получаем список значений
# print(_(_._))
# print(v v _._)

print()
# ######################################################################################################################
# items ()
d = {"a": 1, "b": 2}
# # # # Получаем объект
# print(_._)
# # # # Получаем список кортежей
# print(_(_._))

print()
# ######################################################################################################################
# <Ключ> in <Словарь>
d = {"a": 1, "b": 2}
# print(_  _)  # Ключ существует
# print(_ _)  # Ключ не существует

print()
# ######################################################################################################################
# <Ключ> not in <Словарь>
d = {"a": 1, "b": 2}
# print(_ _) # Ключ не существует
# print(_ _)  # Ключ существует

print()
# ######################################################################################################################
# get ( <Ключ> [, <Значение по умолчанию>] )
d = {"a": 1, "b": 2}
# print(_._(_), _._(_), _._(_, 800))

print()
# ######################################################################################################################
# setdefault (<Ключ> [, <Значение по умолчанию>])
d = {"a": 1, "b": 2}
# print(_.__(_), _.__(_), _.__(_, 0))
# print(_)

print()
# ######################################################################################################################
# рор ( <Ключ> [, <Значение по умолчанию> ])
d = {"a": 1, "b": 2, "c": 3}
# print(_._(_), _._(_, 0))

print()
# ######################################################################################################################
# popitem()
d = {"a": 1, "b": 2}
print(_._())
print(_._())

print()
# ######################################################################################################################
# clear ()
d = {"a": 1, "b": 2}
# _._
# print(_)  # # # Словарь теперь пустой

print()
# ######################################################################################################################
# update ()
# uрdаtе(<Ключ1>=<Значение1>[, ... , <КлючN>=<ЗначениеN>])
d = {"a": 1, "b": 2}
# _._(3, 4)
# print(_)

print()
# ######################################################################################################################
# update ()
# uрdаtе(<Словарь>)
d = {"a": 1, "c": 3, "b": 2, "d": 4}
# _._(c 10 d 20)
# print(_) # Значения элементов перезаписаны

print()
# ######################################################################################################################
# update()
# uрdаtе(<Список кортежей с двумя элементами>)
d = {"a": 1, "c": 3, "b": 2, "d": 4}
# _._(d 80 "e" 6) # Список кортежей
# print(_)

print()
# ######################################################################################################################
# update()
# uрdаtе(<Список списков с двумя элементами>)
d = {"a": 1, "c": 3, "b": 2, "d": 4}
# _._(a str i t)   # Список списков
# print(_)

print()
# ######################################################################################################################
# сору ( )
d1 = {"a": 1, "b": [10, 20]}
# # # # Создаем поверхностную копию
# d2
# # # # Это разные объекты
# print(_ _)
# # # # Изменяем значение
# 800
# # # # Изменилось значение только в d2
# print(_, _)

# # # # Изменяем значение вложенного списка
# new
# # # # Изменились значения и в d1, и в d2!!!
print(_, _)

print()
# ######################################################################################################################
# Генераторы словарей

keys = ["a", "b"]  # Список с ключами
values = [1, 2]  # Список со значениями

# print(k:)
# print(k)

d = {"a": 1, "b": 2, "c": 3, "d": 4 }
# print({k v % 2 == 0})
# # {'b': 2, 'd': 4}

print()
# ######################################################################################################################
# dict keyword argument form
# print(_(name age))

print()
# ######################################################################################################################
# dict key/value tuples form
# print(_(name _), (age _)

print()
# ######################################################################################################################
# Zip together keys and values
# print(_(_(a b c)))

print()
# ######################################################################################################################
# Make a dict from zip result
# D = _(_(a b c))
# print(_)
# print(_)

print()
# ######################################################################################################################
# dict comprehension
# D = k_ v _ (_,_) _ _(a b c, 1 2 3)

print()
# ######################################################################################################################
# dict comprehension
# Or: range(1, 5)
# D = x x**2 _ x 1 2 3 4 5

print()
# ######################################################################################################################
# dict comprehension
# Loop over any iterable

# D = c c*4 _ c SPAM
# print(_)

# D = _._: c + ! _ c _ _SPAM, EGGS, HAM
print(_)

print()
# ######################################################################################################################
# Initialize dict from keys with a comprehension
# D = _._(a b c 0)    # Initialize dict from keys
# print(_)
# # # # Same, but with a comprehension
# D = k__ _ k _ [a b c]

print()
# ######################################################################################################################
# len(d) – количество элементов.

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}
# print(_(_), 'entries found')

print()
# ######################################################################################################################
# d[key]

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

# _:
#     print(Mary: _Mary)
#     print(Lumberjack:, _Lumberjack)
# _ _ _ _:
#     print(No entry for, __._)


print()
# ######################################################################################################################
# d[key] = value
# value – изменить значение или создать новую пару ключ-значение, если ключ не существует.

# phonebook = {
#     'Jack': '032-846',
#     'Guido': '917-333',
#     'Mario': '120-422',
#     'Mary': '890-532',  # последняя запятая игнорируется
# }
#
# phonebook['Lumberjack'] = '000-777'

# ######################################################################################################################
# d[key]
# key in d, key not in d – проверка наличия ключа в отображении.

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

# person (Guido, Mary, Ahmed)

# print(_ is in the phonebook)

# print(No entry found for _)

print()
# ######################################################################################################################
# iter(d) – то же самое, что iter(d.keys()).

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

# print(People in the phonebook:)
# person
# print(_)

print()
# ######################################################################################################################
# copy() – создать неполную копию словаря.

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

# phonebook_copy
# print(Phonebook: _)
# print(Phonebook copy: _)

print()
# ######################################################################################################################
# clear() – удалить все элементы словаря.

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

# __._
# print(Phonebook: _)
# print(Phonebook copy: _)

print()
# ######################################################################################################################
# dict.fromkeys(sequence[, value])

# numbers_dict = _._(_(3), 42)
# print(_)

print()
# ######################################################################################################################
# d.get(key[, default])
# key 5
# print('___'._(_), _._(_, 0))

print()
# ######################################################################################################################
# d.items()

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}
# print(_ _ _._)

print()
# ######################################################################################################################
# d.keys()

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}
# print(Keys:_ _._)

print()
# ######################################################################################################################
# d.values()

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}
# print(Values:_ _._)

print()
# ######################################################################################################################
# d.pop(key[, default])

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

number = _._('Lumberjack')
# print('Deleted Lumberjack (was ' + _ + ')')
print(_)

print()
# ######################################################################################################################
# d.popitem()

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}
# person = _._
# print(Popped __ (phone: __)_(__))

print()
# ######################################################################################################################
# d.setdefault(key[, default])

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}
# person Jack Liz
# phone = _._(__ 000-000)
# print('{} {}'__(_, _))
# print(_)

print()
# ######################################################################################################################
# d.update(mapping)

phonebook = {
    'Jack': '032-846',
    'Guido': '917-333',
    'Mario': '120-422',
    'Mary': '890-532',  # последняя запятая игнорируется
}

# _._(Alex_ 832-438 _ Alice _  231-987)
# _._(Joe_ 217-531)_ (James_ 783-428)
# _._(Carl=783-923_ Victoria=386-486)
# print(_)

# подсчитать количество каждого символа в строке using Counter

# три наиболее частых элемента
# using Counter
C = None


# все уникальные элементы
# using Counter
C = None

# все элементы
# using Counter
C = None

# сумма значений
# using Counter
C = None

# количество букв 'a'
# using Counter
C = None

# добавить новые буквы
# using Counter
C = None

# удалить все 'b'
# using Counter
C = None

# создать новый счётчик
# using Counter
C = None

# добавить его элементы в первый
# using Counter
C = None

# очистить счётчик
# using Counter
C = None

# # внимание: если счёт элемента установить или уменьшить до нуля, он останется в
# # счётчике, пока не будет удалён явно
# using Counter
C = None


# Dictionary keys must be hashable objects. Associated values on the other hand can be any object
# # # List
# # # Tuples
# # # Dictionary
# # # Numbers


# Interestingly, functions are hashable:

def mu_func():
    pass

# # # # Which means we can use functions as keys in dictionaries:
d = None

# We can also create dictionaries using a dictionary comprehension.

keys = ['a', 'b', 'c']
values = (1, 2, 3)

# # # # We can then easily create a dictionary this way - the non-Pythonic way!
# # # # creates an empty dictionary

# # # # But it is much simpler to use a dictionary comprehension:

# list comprehensions - you can have nested loops, if statements, etc.
keys = ['a', 'b', 'c', 'd']
values = (1, 2, 3, 4)

d = None

# create a grid of 2D coordinate pairs, and calculate their distance from the origin:

x_coords = (-2, -1, 0, 1, 2)
y_coords = (-2, -1, 0, 1, 2)

grid = None

import math
grid_extended = None

# # # # We can now easily tweak this to make a dictionary, where the coordinate pairs are the key,
# # # # and the distance the value:

grid_extended = None

# Using fromkeys

counters = None

# # # # If we do not specify a value, then None is used:

# Dictionaries support the len function - this simply returns the number of key/value pairs in the dictionary:
d = None

# Here we have a string where we want to count the number of each character that appears in the string.
# Since we know the alphabet is a-z, we could create a dictionary with these initial keys -
# but maybe the string contains characters outside of that, maybe punctuation marks, emojis, etc.
# So it's not really feasible to take that approach.

text = 'Put here some long text'
# counts = dict()

# We can refine this a bit - first we'll ignore spaces,
# then we'll want to consider lowercase and uppercase characters as the same:

# counts = dict()

# Removing elements from a dictionary
# pop()

d = None

result = None

# Removing elements from a dictionary
# popitem()

d = {'a': 10, 'b': 20, 'c': 30}

# Inserting keys with a default
# Sometimes we may want to insert an element in a dictionary with a default value, but only
# if the element is not already present:

d = {'a': 1, 'b': 2, 'c': 3}

# # # # Function
def insert_if_not_present():
    pass

result = None  # d, 'a', 0
result = None  # d, 'y', 10

# setdefault()
d = {'a': 1, 'b': 2, 'c': 3}
result = None

result = None


# Clearing All Items
d = {'a': 1, 'b': 2, 'c': 3}

# how many times each character occurred in a string:

text = 'Some long text'
counts = None

# how many times each character occurred in a string:
# Suppose now that we just want a dictionary to track the uppercase, lowercase, and other characters in the string
# (i.e. kind of grouping the data by uppercase, lowercase, other) - again ignoring spaces:

import string
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

text = 'Some long text'

categories = None

# ow many times each character occurred in a string:
# We can simplify this a bit using setdefault:

text = 'Some long text'
categories = None

# how many times each character occurred in a string:
#
# Just to clean things up a but more, let's create a small utility function that will return the category key:

text = 'Some long text'

def cat_key():
    pass

categories = None


# how many times each character occurred in a string:
#
# If you are not a fan of using if...elif... in the cat_key function we could do it this way as well

text = 'Some long text'

def cat_key():
    pass

# cat_key('a'), cat_key('A'), cat_key('!'), cat_key(' ')

categories = None


# how many times each character occurred in a string:
#
# We could also do it this way, creating a categories dictionary that has all the individual characters we are interested in:

# chain

def cat_key():
    pass


# We can iterate over the keys of a dictionary using the dictionary's iterator directly, or via the keys view:

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 30, 'd': 4, 'e': 5}

# We can iterate over just the values of the dictionary:

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'c': 30, 'd': 4, 'e': 5}


# # # # and over the items, as tuples, of the dictionary:

# # # # We can also unpack the tuples directly while iterating:

# # # # These views are iterables, not just iterators:

# Let's say we have two dictionaries, and we want to create a new dictionary that contains all the items
# whose keys are in both dictionaries. We want the value in the new dictionary to be a tuple containing all the values from both dictionaries:

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}

k1 = None
k2 = None

# # # # So we have now identified the common keys, all that's left to do is build a dictionary from those keys and the corresponding values.

new_dict = None

# # # # But, a dictionary comprehension would be a better approach here:

new_dict = None

# Let's tweak this a bit and generate a new dictionary, again containing just the common keys,
# but whose value is either the common value, or if the underlying dictionaries have different values for the same key,
# choose the values from the second dictionary, discarding the values from the first.

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 30, 'd': 4}

new_dict = None

# suppose we have two dictionaries, and we want to identify items whose keys are not common to both dictionaries

d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'a': 10, 'b': 20, 'c': 30, 'e': 5}

union = None
intersection = None
keys = None

result = None

# # # # Or, better yet, we could use a dictionary comprehension:

# In this example we have some dictionaries we use to configure our application.
# One dictionary specifies some configuration defaults for every configuration parameter our application will need.
# Another dictionary is used to configure some global configuration,
# and another set of dictionaries is used to define environment specific configurations, maybe dev and prod.


conf_defaults = None  # host', 'port', 'user', 'pwd', 'database'

conf_global = {
    'port': 5432,
    'database': 'deepdive'}

conf_dev = {
    'host': 'localhost',
    'user': 'test',
    'pwd': 'test'
}

conf_prod = {
    'host': 'prodpg.deepdive.com',
    'user': '$prod_user',
    'pwd': '$prod_pwd',
    'database': 'deepdive_prod'
}

# # # # Now we can generate a full configuration for our dev environment this way:

config_dev = None

# # # # and a config for our prod environment:

config_prod = None
