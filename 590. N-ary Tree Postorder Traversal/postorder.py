# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-02 22:06:31
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-02 22:37:45
class Solution(object):
	res = []
	def traverse(self, root):
		if not root:
			return
		else:
			if root.children:
				return 1
			for child in root.children: # root.children is a list
				self.traverse(child)
			self.res.append(root.val)
		return 
	def postorder(self, root):
		if not root:
			return []
		else:
			self.res = []
			self.traverse(root)
			return self.res
