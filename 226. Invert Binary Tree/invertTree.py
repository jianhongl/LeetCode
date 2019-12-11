#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2/12/19 9:52 am
# @Author  : Jianhongl
# @Site    : 
# @File    : invertTree.py
# @Software: PyCharm

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution:
    def invertTree(self, root):
        '''
        :param root: TreeNode
        :return: TreeNode
        '''
        if not root:
            return None
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root





tree = TreeNode([4,2,7,1,3,6,9])
solution = Solution()
print(solution.invertTree(tree))
