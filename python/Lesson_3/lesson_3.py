# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## heller.ru/course
## lesson 3
## http://heller.ru/course/viewtopic.php?f=7&t=30
## https://github.com/SergeyTrunov/course/tree/master/python/Lesson_3
##----------------------------------------------------------------------


DEBUG = True # False # 

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

def sieve(n):
    """
    возвращает список всех простых чисел вплоть до n
    """
    full_table  = range(2,n)
    prime_table = range(2,n)
    for i in range(len(prime_table)):
        if DEBUG:
            print(i, prime_table[i] )

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
sieve(10)


