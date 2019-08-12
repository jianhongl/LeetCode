# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-13 00:23:47
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-13 00:34:42
class Solution(object):
	def relativeSortArray(self, arr1, arr2):
		res = []
		for elem in arr2:
			i = 0
			while i < len(arr1):
				if arr1[i] == elem:
					res.append(arr1.pop(i))
				else:
					i = i + 1
		arr1.sort()
		return res + arr1
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
solution = Solution()
print(solution.relativeSortArray(arr1,arr2))

		