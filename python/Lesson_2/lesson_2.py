# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## heller.ru/course
## lesson 2
## http://heller.ru/course/viewtopic.php?f=7&t=24#p367
## https://github.com/SergeyTrunov/course/tree/master/python/Lesson_2
##----------------------------------------------------------------------
import math
import time

DEBUG = False # True 

def is_int(a):
    """
    check: input is int?
    """
    try:
        int(a)
        if str(a)==str(int(a)):
            return True
        return False
    except:
        return False

def input_int(a, b):
    """
    input int number beetwin a & b
    """
    # check correct a & b
    if is_int(a) == False:
        return "первый аргумент вызова функции не целое число"
    if is_int(b) == False:
        return "второй аргумент вызова функции не целое число"
    if int(b) <= int(a):
        return "второй аргумент вызова функции должен быть больше первого"
    while True:
        print("введите целое число из интервала %s и %s" % (a , b))
        i = input()
        if is_int(i) == False:
            continue
        if (int(i) > int(a)) and (int(i) < int(b)):
            return i

def is_prime(a):
    """
    is prime
    """
    number=int(a)
    i=2 
    while i<number:
        if number % i == 0:
            if DEBUG==True:
                print(i) # с нулевым остатком от деления
            return False
        i+=1
    return True

import math

def maximum_prime(s):
    """
    maximum prime
    s = a x b
    """
    price=1
    if is_int(s) == False:
        return "аргумент вызова функции не целое число"

    int_a=[] # массив простых чисел, на которые s делится без остатка

    # s = a * b
    # в первом проходе проверяем на: 
    # на нулевой остаток от деления s \ a (запоминаем такие a в массив)
    # на то, что b - простое число
    # первый проход, a от 2 до sqrt(a)
    max=int(math.sqrt(int(s))) 
    a=2
    while a<=max:
        if s % a == 0:
            b = int(s / a)
            if DEBUG==True:
                print(b) # с нулевым остатком от деления
            if is_prime(b):
                r=[s,b]
                return r
            else:
                int_a.append(a)
        a+=1

    # второй проход
    # проверяем найденные ранее a на простое или нет,
    # начиная с конца массива
    i = len(int_a)
    while i>0:
        a=int_a[i-1]
        if is_prime(a):
            r=[s,a]
            return r
        i-=1

    # заданное число - простое
    r=[s,s]
    return r

def compare_functions(f, g, arg):
    """
    compare functions function1(arg) and function2(arg)
    """
    i = 0
    t1 = 0
    t2 = 0
    while i < 1000:
      last_time = time.clock()
      f(arg)
      t1 += time.clock() - last_time
      last_time = time.clock()
      g(arg)
      t2 += time.clock() - last_time
      i += 1
    print(t2 / t1)


# 2.3
def fibo_old(n):
    """
    вычисление числа ФИбоначчи
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if n == 0: return 0
    if n == 1: return 1
    return fibo_old(n - 1) + fibo_old(n - 2)

def fibo_comment(n):
    """
    вычисление числа ФИбоначчи
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    print("Начинаю вычислять число Фибоначчи:" + str(n))
    if n == 0: 
        result=0 
        print(" F(" + str(n) + ")=" + str(result))
        return result

    if n == 1: 
        result=1
        print(" F(" + str(n) + ")=" + str(result))
        return result

    result = fibo_comment(n - 1) + fibo_comment(n - 2)
    print("Вычислил F(" + str(n) + ")=" + str(result))
    return result

def fibo_new(n):
    """
    вычисление числа ФИбоначчи
    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if is_int(n) == False:
        return "аргумент вызова функции не целое число"

    FNmin2 = 0
    FNmin1 = 1
    FN     = 0 
    if n==0:
        FN = 0 
        if DEBUG==True:
            print("F("+str(n)+")="+str(FN)) 
        return FN
    if n==1:
        FN = 1 
        if DEBUG==True:
            print("F("+str(n)+")="+str(FN)) 
        return FN
    i=2
    while i<=n:
        FN = FNmin2 + FNmin1
        FNmin2 = FNmin1
        FNmin1 = FN
        if DEBUG==True:
            print("F("+str(i)+")="+str(FN)) 
        i+=1
    if DEBUG==True:
        print("F("+str(i-1)+")="+str(FN)) 
    return FN

#
# main
# 

# 2.1
# print(input_int(1, 23))

# 2.2
# i=20000
# while i<20030:
#    print(i,":",int(math.sqrt(i)),":",maximum_prime(i))
#    i+=1

# 2.3
# fibo_comment(4)

# 2.4
# n = 20
# print("Функция с рекурсией.  F(" + str(n) + ")=" + str(fibo_old(n)))
# print("Функция без рекурсии. F(" + str(n) + ")=" + str(fibo_new(n)))
# compare_functions(fibo_old, fibo_new, n)
#
# Функция с рекурсией.  F(15)=610
# Функция без рекурсии. F(15)=610
# 0.008011137226276631
#
# Функция с рекурсией.  F(20)=6765
# Функция без рекурсии. F(20)=6765
# 0.0009779885958742225







