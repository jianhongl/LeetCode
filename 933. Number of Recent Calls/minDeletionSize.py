# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-02 20:20:10
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-02 21:20:55
class Solution(object):
	def minDeletionSize(self, A):
		size = len(A[0])
		fst_check = []
		D = 0		
		possible = 0
		while possible < size:
			fst_check = []
			for elem in A:
				fst_check.append(elem[possible])
			reverse_check = sorted(fst_check)
			# sort()与sorted()的不同在于，sort是在原位重新排列列表，而sorted()是产生一个新的列表。
			if fst_check == reverse_check:
				possible += 1
			else:
				D += 1
				possible += 1
		return D



test = ["zyx","wvu","tsr"]
solution = Solution()
print(solution.minDeletionSize(test))

		