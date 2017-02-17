#!/usr/bin/env python
# coding=utf-8

def counter():
    count = [0]

    def incer():
        count[0] = count[0] + 1

        return count
    return incer

