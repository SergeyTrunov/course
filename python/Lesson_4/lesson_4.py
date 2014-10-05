# -*- coding: utf-8 -*-
##----------------------------------------------------------------------
## heller.ru/course
## lesson 4
## http://heller.ru/course/viewtopic.php?f=7&t=43
## https://github.com/SergeyTrunov/course/tree/master/python/Lesson_4
##----------------------------------------------------------------------

import time

DEBUG = False # True # 

class Logger:
    def __init__(self):
        self.file = open("error.log", "a")
        self.level = 1
        self.messages = []

    def write(self, string, level):
        if level > self.level: return
        message = str(time.ctime())
        message += ": "
        message += string
        message += "\n"
        self.file.write(message)
        self.file.flush()
        self.messages.append(message)

    def setLogLevel(self, level):
        self.level = level

    def __getitem__(self, index):
        return self.messages[-index]

    def __len__(self):
        return len(self.messages)

#log = Logger() # создаём логгер
#log.setLogLevel(3) # логируем все сообщения 
#log.write("Логгер работает!", 3) # пишем сообщение в лог-файл

