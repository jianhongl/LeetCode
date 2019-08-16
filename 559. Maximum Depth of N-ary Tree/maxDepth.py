# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-16 20:25:18
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-16 21:17:13
class Solution(object):
	def maxDepth(self, root):
		"""
		:type root: Node
		:rtype: int
		"""
		if not root:
			return 0
		else:
			if root.children:
				return 1 + max(self.maxDepth(child) for child in root.children)
			else:
				return 1
        
		