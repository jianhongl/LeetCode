# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-22 16:34:25
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-22 20:12:34
# 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
	def mergeTrees(self, t1, t2):
		if not t1 and t2:
			return t2
		elif not t2 and t1:
			return t1
		elif not t2 and not t1:
			return None
		else:
			t3 = TreeNode(t1.val + t2.val)
			t3.left = self.mergeTrees(t1.left, t2.left)
			t3.right = self.mergeTrees(t1.right, t2.right)
			return t3

