# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## heller.ru/course
## lesson 3
## http://heller.ru/course/viewtopic.php?f=7&t=30
## https://github.com/SergeyTrunov/course/tree/master/python/Lesson_3
##----------------------------------------------------------------------

import types
import random
import string
import json
import math
import time

DEBUG = False # True # 

# 3.5
# map, filter

def add1(x): 
    return x*x

add2 = lambda x: x*x

def filter1(x): 
    if x < 4:
        return x

filter2 = lambda x: x < 4

# Задание 3.5.Для работы со всеми перечислимыми объектами Python 
# предлагает функции map и filter. Прочитайте про эти функции и реализуйте 
# сами собственные функции my_map и my_filter, которые работают точно так же как map и filter.

def my_map(arg ,f):
  """
  map fnction
  """
  map_list = []
  for a in arg:
    map_list.append(f(a))

  return map_list

# print(my_map([1,2,3,4,5], add1))
# print(my_map([1,2,3,4,5], add2))

def my_filter(arg, f):
  """
  filter fnction
  """
  filter_list = []
  for a in arg:
    if f(a):
        filter_list.append(a)

  return filter_list

# print(my_filter([1,2,3,4,5], filter1))
# print(my_filter([1,2,3,4,5], filter2))


