#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/12/19 1:53 pm
# @Author  : Jianhongl
# @Site    : 
# @File    : findUnsortedSubarray.py
# @Software: PyCharm
class Solution:
    def findUnsortedSubarray(self, nums):
        '''

        :param nums:List[int]
        :return: int
        '''
        n = len(nums)
        print(nums)
        order = sorted(nums)
        start = nums[0]
        end = nums[0]
        if n == 1:
            return 0
        if nums == order:
            return 0
        for i in range(n):
            if order[i] != nums[i]:
                start = i
                break
        for j in range(n-1,-1,-1):
            if order[j] != nums[j]:
                end = j
                break
        print(start, end)
        return end - start + 1
nums = [1,3,2,2,2]
solution = Solution()
print(solution.findUnsortedSubarray(nums))

