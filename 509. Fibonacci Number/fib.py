# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-16 20:00:39
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-16 20:12:07
class Solution(object):
	def fib(self, N):
		# if N < 1:
		# 	return 0
		# elif N == 1:
		# 	return 1
		# else:
		# 	return self.fib(N-1) + self.fib(N-2)
		if N > 0 :
			if N <= 1:
				return N
			else:
				return self.fib(N-1) + self.fib(N-2)
		else:
			return 0

solution = Solution()
print(solution.fib(3))