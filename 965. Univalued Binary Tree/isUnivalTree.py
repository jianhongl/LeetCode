# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-12 23:01:14
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-13 00:17:31
class Solution(object):
	lst = []
	def __init__(self):
		pass
	def isUnivalTree(self, root):
		self.lst = []
		if not root:
			return None
		else:
			flag = True
			self.TreetoList(root)
			print(self.lst)
			for elem in self.lst:
				if elem == self.lst[0]:
					continue
				else:
					flag =False
					return flag
			return flag
	def TreetoList(self, root):
		if root.left is not None:
			self.TreetoList(root.left)
		if root.right is not None:
			self.TreetoList(root.right)
		self.lst.append(root.val)

        
solution = Solution()
print(solution.isUnivalTree([1,1,1,1,1,None,1]))

		