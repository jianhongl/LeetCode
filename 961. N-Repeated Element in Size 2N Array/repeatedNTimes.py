# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-22 15:21:29
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-22 15:26:16
class Solution(object):
	def repeatedNTimes(self, A):
		lst = list()
		for elem in A:
			if elem not in lst:
				lst.append(elem)
				print(lst)
			else:
				return elem

A = [1,2,3,3]
solution = Solution()
print(solution.repeatedNTimes(A))