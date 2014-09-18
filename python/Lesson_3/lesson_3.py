# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## heller.ru/course
## lesson 3
## http://heller.ru/course/viewtopic.php?f=7&t=30
## https://github.com/SergeyTrunov/course/tree/master/python/Lesson_3
##----------------------------------------------------------------------

import random
import string

DEBUG = False # True # 

def is_number(x): 
    """
    is number x
    
    """
    list_x = list(str(x))
    if DEBUG:
        print(x, list_x)

    for i in range(len(list_x)):
        if   list_x[i]=='0':
            continue
        elif list_x[i]=='1':
            continue
        elif list_x[i]=='2':
            continue
        elif list_x[i]=='3':
            continue
        elif list_x[i]=='4':
            continue
        elif list_x[i]=='5':
            continue
        elif list_x[i]=='6':
            continue
        elif list_x[i]=='7':
            continue
        elif list_x[i]=='8':
            continue
        elif list_x[i]=='9':
            continue
        elif list_x[i]=='.':
            continue
        elif list_x[i]=='-':
            continue
        #elif list_x[i]==' ':
        #    continue
        #elif list_x[i]=='+':
        #    continue
        else:
            return False

    return True

def sieve_full(n):
    """
    возвращает список всех простых чисел вплоть до n
    алгоритм "Решето Эратосфена"
    все по честному: вычеркиваем повторно, проверяем каждый элемент от 2 до n

    """
    table = [True for table in range(n + 1)]
    prime_table = []

    # вычеркиваем из натуральных
    i = 2
    while i <= n:
        if DEBUG:
            print(i, table[i] )
        j = i + i
        while j <=n:
            table[j] = False
            j+=i
        i+=1

    # собираем оставшиеся
    i = 2
    while i <= n:
        if table[i] == True:
            if DEBUG:
                print(i, table[i] )
            prime_table.append(i)
        i+=1

    return prime_table

def sieve(n):
    """
    возвращает список всех простых чисел вплоть до n
    алгоритм "Решето Эратосфена"
    модификации: 
    - перебираем натуральные от 2 до корня квадратного из n
    - первое число для вычеркивания берем i * i

    """
    table = [True for table in range(n + 1)]
    prime_table = []

    # вычеркиваем из натуральных
    i = 2
    while i * i <= n:
        if DEBUG:
            print(i, table[i] )
        j = i * i
        while j <=n:
            table[j] = False
            j+=i
        i+=1

    # собираем оставшиеся
    i = 2
    while i <= n:
        if table[i] == True:
            if DEBUG:
                print(i, table[i] )
            prime_table.append(i)
        i+=1

    return prime_table

def random_phone_book(n):
    """
    телефон --- просто семизначное число (случайное), уникальное
    имя --- это случайная строка символов английского алфавита, имеющая какую-то случайную длину от 4 до 10 символов
    """
    f = open('random_phone_book.dat', 'w')
    phone=[]
    name=[]
    i = 0
    # сформирум книгу
    while i <= n:
        random_phone = random.randint(1000000,9999999)
        random_name = "".join(random.sample(string.ascii_letters,random.randint(4,10)))
        if random_phone not in phone:
            phone.append(str(random_phone))
            name.append(random_name)
            if DEBUG:
                print(i, random_phone, random_name)
            i+=1
    # записать в файл
    i = 0
    while i <= n:
        f.write(phone[i] + ":" + name[i] + '\n')
        i+=1

    f.close()

    return phone, name


#
# main
#

# 3.1 (в рамках задания)
# print("-234.12 is number: ", is_number("-234.12"))
# print("asdf is number: ", is_number("asdf"))
# print("2,44 is number: ", is_number("2,44"))
# print("12 304.22 is number: ", is_number("12 304.22"))
# print("+1.06 is number: ", is_number("+1.06"))
#
# -234.12 is number:  True
# asdf is number:  False
# 2,44 is number:  False
# 12 304.22 is number:  False
# +1.06 is number:  False
# 

# 3.2 Решето Эратосфена
# print(sieve_full(101))
# print(sieve(101))

# 3.2*
# "На самом деле приведённый там код - это не решето Эратосфена, 
# а его подобие, которое работает на порядок хуже оригинального алгоритма. 
# (Задание со звёздочкой - объясните чем хуже алгоритм из Википедии)"
# ru.wikipedia.org/wiki/Решето_Эратосфена
# не разобрался: 
# 1. что называть оригинальным алгоритмом
# 2. какую реализиацию разбирать
# если считать оригинальным алгоритмом  с условиями "вычеркиваем повторно, проверяем каждый элемент от 2 до n",
# то каждая из реализаций на вике оптимальнее


# 3.4
print(random_phone_book(100))

