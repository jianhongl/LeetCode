# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-12 22:37:32
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-12 22:55:22
class Solution(object):
	def sortArrayByParityI(self, A):
		j = 0
		res = []
		odd = []
		even = []
		for elem in A:
			if elem % 2 == 0:
				even.append(elem)
			else:
				odd.append(elem)
		while j < len(A):
			if j % 2 == 0:
				res.append(even.pop())
				j = j + 1
			else:
				res.append(odd.pop())
				j = j + 1 
		return res
A = [4,2,5,7]
solution = Solution()
print(solution.sortArrayByParityIi(A))




		