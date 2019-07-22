# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-22 15:12:31
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-22 15:15:53
class Solution(object):
	def sortArrayByParity(self, A):
		i = 0
		rest =list()
		while i < len(A):
			if A[i] % 2 == 0:
				i = i + 1
				continue
			else:
				rest.append(A.pop(i))
		return A+rest
A = [3,1,2,4]
solution = Solution()
print(solution.sortArrayByParity(A))
		