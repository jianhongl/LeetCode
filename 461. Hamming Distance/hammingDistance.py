# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-23 13:05:06
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-23 14:08:26
class Solution:
	def hammingDistance(self, x, y):
		count = 0
		res = ""
		x_bits = self.digit_to_bin(x, res)
		y_bits = self.digit_to_bin(y, res)
		pos1 = 0
		pos2 = 0
		if len(x_bits) < len(y_bits):
			for i in range(len(y_bits)-len(x_bits)):
				x_bits += '0'
		else:
			for i in range(len(x_bits)-len(y_bits)):
				y_bits += '0'
		j = 0
		while j < len(x_bits):
			if x_bits[j] != y_bits[j]:
				count += 1
				j = j + 1
			else:
				j = j + 1
		return count


	def digit_to_bin(self, a, res):
		if a == 0:
			res += '0'
			return res
		elif a == 1:
			res += '1'
			return self.digit_to_bin(0,res)
		else:
			res += str(a % 2)
			return self.digit_to_bin(a // 2, res)


solution = Solution()
print(solution.hammingDistance(3,1))