#!/usr/bin/env python
# coding=utf-8

#装饰器函数
def doc_func(func):
    #此处写包裹函数（闭包，额外需要添加的新功能全部在此函数中）
    def warpfunc():
        #做一些额外的事情
        print "%s called" %(func.__name__)
        func()
    return warpfunc

@doc_func
def foo():
    print "hello"

@doc_func
def bar():
    print "world"

if __name__ == "__main__":
    foo()
    bar()

