#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 10/12/19 9:50 am
# @Author  : Jianhongl
# @Site    : 
# @File    : rob.py
# @Software: PyCharm
from typing import List


class  Solution:
    # recursion and memoization
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     total_amount = [-1]*n
    #
    #     def rob_(nums, i):
    #         if i < 0:
    #             return 0
    #         if total_amount[i] >= 0:
    #             return total_amount[i]
    #         total_amount[i] = max(rob_(nums, i-2) + nums[i], rob_(nums, i-1))
    #         return total_amount[i]
    #
    #     return rob_(nums, n-1)
    def rob(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        else:
            dp = [0] * n
            for i in range(n):
                # dp是已经经过了i个房子，之前的房子可以抢也可以不抢. dp 用来记录之前经过房子的最大值
                dp[i] =max((dp[i-2]+nums[i] if i > 1 else nums[i]), (dp[i-1] if i > 0 else 0))
        return dp[-1]
nums = [1,2,3,1]
solution = Solution()
print(solution.rob(nums))








