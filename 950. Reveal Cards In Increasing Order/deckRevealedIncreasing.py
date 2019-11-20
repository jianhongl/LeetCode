#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 20/11/19 10:01 am
# @Author  : Jianhongl
# @Site    : 
# @File    : deckRevealedIncreasing.py
# @Software: PyCharm
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort() # this is the result of this game
        unrevealed = []
        while len(deck) > 0:
            unrevealed.append(deck.pop())
            if len(deck) > 0:
                unrevealed.append(unrevealed.pop(0))
        unrevealed.reverse()
        return unrevealed

deck = [17,13,11,2,3,5,7]
solution = Solution()
print(solution.deckRevealedIncreasing(deck))


