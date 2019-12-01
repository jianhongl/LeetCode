#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 20/11/19 2:41 pm
# @Author  : Jianhongl
# @Site    : 
# @File    : queensAttacktheKing.py
# @Software: PyCharm
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        result = []
        dia1 = []
        dia2 = []
        dia3 = []
        dia4 = []
        x_top, x_bottom = self.check_same_col(queens, king)
        y_left, y_right = self.check_same_row(queens, king)
        left = [x for x in queens if x not in (x_top and x_bottom and y_right and y_left)]
        print(left)
        if len(x_top) != 0:
            x_top.sort()
            result.append(x_top[-1])
        if len(x_bottom) != 0:
            x_bottom.sort()
            result.append(x_bottom[0])
        if len(y_left) != 0:
            y_left.sort()
            result.append(y_left[-1])
        if len(y_right) != 0:
            y_right.sort()
            result.append(y_right[0])
        for elem in left:
            if self.check_diagnal(elem, king):
                if elem[0] < king[0] and elem[1] < king[1]:
                    dia1.append(elem)
                elif elem[0] > king[0] and elem[1] > king[1]:
                    dia4.append(elem)
                elif elem[0] > king[0] and elem[1] < king[1]:
                    dia3.append(elem)
                else:
                    dia2.append(elem)
        if len(dia1) != 0:
            dia1.sort()
            result.append(dia1[-1])
        if len(dia2) != 0:
            dia2.sort()
            result.append(dia2[-1])
        if len(dia3) != 0:
            dia3.sort()
            result.append(dia3[0])
        if len(dia4) != 0:
            dia4.sort()
            result.append(dia4[0])
        return result


    def check_same_col(self, queens, king):
        x_top = []
        x_bottom = []
        for queen in queens:
            if queen[0] == king[0]:
                if queen[1] < king[1]:
                    x_top.append(queen)
                else:
                    x_bottom.append(queen)
        return x_top, x_bottom

    def check_same_row(self, queens, king):
        y_right = []
        y_left = []
        for queen in queens:
            if queen[1] == king[1]:
                if queen[0] < king[0]:
                    y_left.append(queen)
                else:
                    y_right.append(queen)
        return y_left, y_right

    def check_diagnal(self,queen, king):
        if abs(queen[0] - king[0]) == abs(queen[1] - king[1]):
            return True
        else:
            return False



queens =[[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
king =[3,4]
solution = Solution()
print(solution.queensAttacktheKing(queens,king))
