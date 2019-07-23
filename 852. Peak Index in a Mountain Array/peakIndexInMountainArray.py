# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-23 15:08:48
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-23 15:17:17
class Solution:
	def peakIndexInMountainArray(self, A):
		i = 0
		while i < len(A):
			if A[i] < A[i+1]:
				i = i + 1
				continue
			elif A[i] > A[i+1]:
				return i
solution = Solution()
print(solution.peakIndexInMountainArray([0,2,1,0]))

# class Solution:
# 		def peakIndexInMountainArray(self, A):
# 			return A.index(max(A))