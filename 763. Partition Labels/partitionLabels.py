#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 14/1/20 10:09 am
# @Author  : Jianhongl
# @Site    : 
# @File    : partitionLabels.py
# @Software: PyCharm
class Solution:
    # BF
    # def partitionLabels(self, S):
    #     '''
    #
    #     @param S: str
    #     @return: List[int]
    #     '''
    #     ans = []
    #     start, end = 0, 0
    #     for i in range(len(S)):
    #         end = max(end, S.rfind(S[i]))
    #         if i == end:
    #             ans.append(end - start + 1)
    #             start = end + 1
    #     return ans

    # Greedy
    def partitionLabels(self, S):
        last_index = {}
        for i, ch in enumerate(S):
            last_index[ch] = i
        start = end = 0
        ans = []
        for i, ch in enumerate(S):
            end = max(end, last_index[ch])
            if i == end:
                ans.append(end - start + 1)
                start = end  + 1
        return ans



S = "ababcbacadefegdehijhklij"
solution = Solution()
print(solution.partitionLabels(S))

