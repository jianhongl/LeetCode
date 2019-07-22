# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-22 14:55:34
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-22 15:02:42
class Solution(object):
	def flipAndInvertImage(self, A):
		hori_A = list()
		for elem in A:
			hori_A.append(elem[::-1])
		i = 0
		while i < len(hori_A):
			j = 0
			while j < len(hori_A[i]):
				if hori_A[i][j] == 0:
					hori_A[i][j] = 1
				else:
					hori_A[i][j] = 0
				j = j + 1
			i = i + 1
		return hori_A

A = [[1,1,0],[1,0,1],[0,0,0]]
solution = Solution()
print(solution.flipAndInvertImage(A))