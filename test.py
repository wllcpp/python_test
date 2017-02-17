#!/usr/bin/env python
# coding=utf-8
my_dict = {"name" : "zhang3", "age" : 18}

for item in my_dict.items():
    print "key = " + item[0]
    print "value = " + str(item[1])

print "*" * 20

for key in my_dict.keys():
    print key + " = " + str(my_dict[key])


