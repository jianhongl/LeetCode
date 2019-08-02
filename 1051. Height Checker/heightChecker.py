# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-02 21:28:06
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-02 21:39:09
class Solution(object):
	def heightChecker(self, heights):
		standard = sorted(heights)
		res = 0
		i = 0 
		while i < len(heights):
			if standard[i] != heights[i]:
				res += 1
				i += 1
			else:
				i += 1
		return res

height = [1,1,4,2,1,3]
solution = Solution()
print(solution.heightChecker(height))
		