#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 30/11/19 10:58 am
# @Author  : Jianhongl
# @Site    : 
# @File    : reconstructQueue.py
# @Software: PyCharm
class Solution:
    def reconstructQueue(self, people):
        '''
        :param people: List[List[int]]
        :return: List[List[int]]
        '''
        result = []
        # 先用第一个关键字逆排序，然后在用第二关键字正向排序
        height_ascent = sorted(people, key=lambda x: (-x[0],x[1]))
        for height, pos in height_ascent:
            result.insert(pos, [height, pos])
        return result


people =[[0,0],[6,2],[5,5],[4,3],[5,2],[1,1],[6,0],[6,3],[7,0],[5,1]]
solution = Solution()
print(solution.reconstructQueue(people))
