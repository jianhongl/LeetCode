#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 9/12/19 8:40 pm
# @Author  : Jianhongl
# @Site    : 
# @File    : pathSum.py
# @Software: PyCharm
class Solution:
    def pathSum(self, root, sum):
        '''
        :param root: TreeNode
        :param sum: int
        :return: int
        '''
        res = []
        if root is None:
            return None
        self.dfs(root, res, [], sum)
        print(res)
        return len(res)

    def dfs(self, root, res, path, sum):
        if sum == 0:
            res.append(path)
            return
        if sum - root.val < 0:
            if root.left and root.right:
                self.dfs(root.left, res, path, sum)
                self.dfs(root.right, res, path, sum)
            elif root.left:
                self.dfs(root.left, res, path, sum)
            elif root.right:
                self.dfs(root.right, res, path,sum)
            else:
                return None
        elif sum - root.val == 0:
            path += [root.val]
            res.append(path)
            return
        else:
            if root.left and root.right:
                self.dfs(root.left, res, path+[root.val], sum - root.val)
                self.dfs(root.right, res, path+[root.val], sum - root.val)
            elif root.left:
                self.dfs(root.left, res, path + [root.val], sum - root.val)
            elif root.right:
                self.dfs(root.right, res, path + [root.val], sum - root.val)
            else:
                return None
