# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-20 15:10:50
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-20 15:14:39
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = list(J)
        stone = list(S)
        count = 0
        for j in jewels:
            for s in stone:
                if j == s:
                    count += 1
                else:
                    continue
        return count
