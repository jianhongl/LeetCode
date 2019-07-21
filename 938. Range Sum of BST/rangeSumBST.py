# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-21 13:45:49
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-21 14:16:44
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    	sumBST = 0
    	# if the tree is null, it will return -1
    	if root is None:
    		return -1
    	# if the val is between L and R, it will add it to the sumBST.
    	if root.val >= L and root.val <= R:
    		sumBST = sumBST + root.val
    	# if the tree has left child, and root's value is greater than L, we will
    	# think about the left child value. If the root's value is less than L, its 
    	# left child must be less than L.
    	if root.left and root.val >= L:
    		sumBST = sumBST + self.rangeSumBST(root.left, L, R)
    	# if the tree has right child, and root's value is less than R, we will
    	# think about the right child value. If the root's value is greater than R, its 
    	# right child must be greater than R.
    	if root.right and root.val <= R:
    		sumBST = sumBST + self.rangeSumBST(root.right, L, R)
    	return sumBST

