# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-22 16:10:39
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-22 16:30:20
class Solution:
	def selfDividingNumbers(self, left, right):
		lst = range(left,right+1)
		res = list()
		if right < 10:
			res.append(range(left,right+1))
			return res
		for elem in lst:
			temp = ""
			flag = False
			if elem < 10:
				res.append(elem)
			else:
				temps = str(elem)
				for temp in temps:
					print(temp)
					try:	
						if elem % int(temp) == 0:
							flag = True
							continue
						else:
							flag = False
							break
					except:
						flag = False
						break
				if flag == True:
					res.append(elem)
				else:
					continue
		return res
left = 1
right = 101
solution = Solution()
print(solution.selfDividingNumbers(left,right))

