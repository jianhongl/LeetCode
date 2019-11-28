#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 28/11/19 1:12 pm
# @Author  : Jianhongl
# @Site    : 
# @File    : maxAreaOfIsland.py
# @Software: PyCharm
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = max(result,self.dfs(i, j, m, n, grid))
        return result

    def dfs(self, x, y, m, n, grid):
        step = ((0,1),(0,-1),(1,0),(-1,0))
        if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == 0:
            return 0
        else:
            count = 1
            grid[x][y] = 0
            for i, j in step:
                count += self.dfs(x+i, y+j, m, n, grid)
            return count





grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
solution = Solution()
print(solution.maxAreaOfIsland(grid))

