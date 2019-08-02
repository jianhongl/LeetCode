# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-08-02 21:43:33
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-08-02 21:59:28
class Solution(object):
	def searchBst(self, root, val):
		if not root:
			return None
		if val < root.val and root.left:
			return self.searchBst(root.left, val)
		elif val > root.val and root.right:
			return self.searchBst(root.right, val)
		elif val == root.val:
			return root
		else:
			return None