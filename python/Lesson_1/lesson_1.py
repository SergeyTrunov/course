# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## heller.ru/course
## lesson 1
## http://heller.ru/course/viewtopic.php?f=7&t=11
## https://github.com/SergeyTrunov/course/tree/master/python/Lesson_1
##----------------------------------------------------------------------


from random import randint

my_number = str(randint(1,101))
valid_number = [str(i) for i in range(1, 101)]
input_number = ''
entries_number = []

DEBUG = False # True

if DEBUG:
    print("загаданное число:", my_number)
    print("допустимые числа:", valid_number)

print("Угадайте число от 1 до 100(включительно)")
print("для выхода введите Q")
print("Я задумал число, начинаем")

while input_number not in (my_number, 'Q'):
    print("ваше число:")
    input_number=input()
    if input_number in valid_number:
        if input_number not in entries_number:
            entries_number.append(input_number)
            if input_number == my_number:
                print("ура вы победили!")   
                if len(entries_number) == 1:
                    print("вы угадали с первой попытки!")
                elif len(entries_number) == 2:
                    print("вы угадали со второй попытки!")
                else:
                    print("вы угадали c", len(entries_number), "попытки")
            elif int(my_number) > int(input_number):
                print("мое число больше вашего")   
            elif int(my_number) < int(input_number):
                print("мое число меньше вашего")   
        else:
            print("такое число уже было, придумайте другое") 						  
        if DEBUG:
            print("использованные числа:", entries_number)
    else:
        print("а это непохоже на число от 1 до 100 (для выхода введите Q)") 						  


