#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 6/12/19 10:43 am
# @Author  : Jianhongl
# @Site    : 
# @File    : countSubstrings.py
# @Software: PyCharm
# dp 对于一个 j 到 i（j<i) 的字符串，它是回文串，当且仅当 i 与 j 处值相等并且 j+1 到 i-1 的子串也满足条件
# dp[i, j] = 1                                   if i == j
#          = s[i] == s[j]                        if j = i + 1
#          = s[i] == s[j] && dp[i + 1][j - 1]    if j > i + 1
class Solution:
    def countSubstrings(self,s):
        '''
        :param s: str
        :return: int
        '''
        n = len(s)
        count = 0
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if i - j < 2:
                    dp[j][i] = s[i] == s[j]
                else:
                    dp[j][i] = ((s[i] == s[j]) and (dp[j+1][i-1]))
                if dp[j][i]:
                    count += 1
            dp[i][i] = 1
            count += 1
        return count
s = "aaa"
solution = Solution()
print(solution.countSubstrings(s))
