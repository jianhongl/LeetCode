# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-22 15:49:12
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-22 15:52:40
class Solution:
	def sortedSquares(self, A):
		i = 0
		while i < len(A):
			A[i] = A[i] * A[i]
			i = i + 1
		A.sort()
		return A

A = [-4,-1,0,3,10]
solution = Solution()
print(solution.sortedSquares(A))