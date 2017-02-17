#!/usr/bin/env python
# coding=utf-8
class Student:
    '''
    student class
    '''

    school = "trau"
    def __init__(self, name, age):
        '''
        构造函数
        '''
        self.name = name
        self.__age = age
        print "__init__"

    def ShowMe(self):
        '''
        普通成员函数
        '''
        print "in show()..."
        print self.name
        print self.__age
        print Student.school

    def __del__(self):
        print "__Del__"

if __name__ == "__main__":
    s1 = Student("zhang3", 19)
    s1.ShowMe()

    s1.name = "wang5"
    s1.age = 20
    s1.ShowMe()

    Student.school = "Talimi"

