# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-23 16:33:41
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-23 16:55:40



class Solution:
	def arrayPairSum(self, nums):
		sum1 = 0
		lst = []
		group = []
		nums.sort()
		for elem in nums:
			group.append(elem)
			if len(group) == 2:
				lst.append(group)
				group = []
		for pair in lst:
			sum1 = sum1 + min(pair)
		return sum1 


# class Solution:
# 	def arrayPairSum(self, nums):
# 		sum1 = 0
# 		nums.sort()
# 		for i in range(0,len(nums),2): # range(start, stop[, step])
# 			sum1 += nums[i]
# 		return sum1
solution = Solution()
print(solution.arrayPairSum([1,4,3,2]))

