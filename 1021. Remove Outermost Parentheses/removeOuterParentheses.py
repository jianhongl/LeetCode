# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-21 14:33:12
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-21 19:11:24
# Variable count to store the parentheses matching. If we meet a '(', adding 1 to the count.
# if we meet a ')', minus 1 to the count. When the count is equal to zero, we will try to 
# remove the outer parentheses.
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
    	count = 0
    	previ = 0
    	result = ''
    	# enumerate is the function to change a iterable data object into a indexing sequence
    	# .
    	for i, s in enumerate(S):
    		if s == '(':
    			count += 1
    		else:
    			count -= 1
    		if count == 0:
    			result += S[previ + 1 : i] # <-
    			previ = i + 1
    	return result

