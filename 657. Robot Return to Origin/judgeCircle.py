# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-22 15:57:33
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-22 16:06:17
class Solution:
	def judgeCircle(self, moves):
		x = 0
		y = 0 
		for move in moves:
			if move == 'U':
				y += 1
			elif move == 'D':
				y -= 1
			elif move == 'L':
				x += 1
			elif move == 'R':
				x -= 1
		if x == 0 and y == 0:
			return True
		else:
			return False
moves = "UD"
solution = Solution()
print(solution.judgeCircle(moves))

