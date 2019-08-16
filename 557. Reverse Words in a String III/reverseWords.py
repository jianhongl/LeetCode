# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-16 22:39:40
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-16 22:47:16
class Solution(object):
    def reverseWords(self, s):
        sentence = s.split(" ")
        res = []
        for words in sentence:
        	res.append(words[::-1])
        return " ".join(res)

solution = Solution()
print(solution.reverseWords("Let's take LeetCode contest"))