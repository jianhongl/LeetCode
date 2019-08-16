# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-16 21:34:47
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-16 22:32:23
# clever!!!!
class Solution(object):
	def commonChars(self,A):
		check = list(A[0])
		for word in A:
			newCheck = []
			for c in word:
				if c in check:
					newCheck.append(c)
					check.remove(c)
			check = newCheck
		return check

solution = Solution()
print(solution.commonChars(["bella","label","roller"]))