#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 1/12/19 10:52 am
# @Author  : Jianhongl
# @Site    : 
# @File    : dailyTemperatures.py
# @Software: PyCharm
# class Solution:
#     def dailyTemperatures(self, T):
#         '''
#         :param T: List[int]
#         :return: List[int]
#         '''
#         result = []
#         for i in range(len(T)):
#             max_value = (T[i], i)
#             index = 0
#             for j in range(i+1, len(T)):
#                 if T[j] > max_value[0]:
#                     index = j - max_value[1]
#                     break
#             result.append(index)
#
#         return result
class Solution:
    def dailyTemperatures(self, T):
        '''
        :param T: List[int]
        :return: List[int]
        '''
        stack = []
        wait = [0]*len(T)
        for i in range(len(T)):
            while len(stack) > 0 and T[stack[-1]] < T[i]:
                j = stack.pop()
                wait[j] = i-j
            stack.append(i)
        return wait
T = [73, 74, 75, 71, 69, 72, 76, 73]
solution = Solution()
print(solution.dailyTemperatures(T))



