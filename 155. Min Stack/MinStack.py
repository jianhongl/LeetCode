#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/12/19 10:30 am
# @Author  : Jianhongl
# @Site    : 
# @File    : MinStack.py
# @Software: PyCharm
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.memo = []


    def push(self, x: int) -> None:
        self.memo.append(x)

    def pop(self) -> None:
        self.memo.pop()


    def top(self) -> int:
        return self.memo[-1]

    def getMin(self) -> int:
        return min(self.memo)

minStack =MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack)
print(minStack.getMin())
minStack.pop()
print(minStack)
print(minStack.top())
print(minStack.getMin())
