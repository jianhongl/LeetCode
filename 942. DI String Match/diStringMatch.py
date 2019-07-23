# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-23 14:12:38
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-23 15:03:53
# 
# Algorithm:
# Keep track of the smallest and largest element we haven't placed. 
# If we see an 'I', place the small element; otherwise place the large element.
class Solution:
	def diStringMatch(self, S):
		if not S:
			return []
		res = []
		l = 0
		r = len(S) 
		for elem in S:
			if elem == 'D':
				res.append(r)
				r -= 1
			else:
				res.append(l)
				l += 1
		res.append(r)
		return res

solution = Solution()
print(solution.diStringMatch("IDID"))