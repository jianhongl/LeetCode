# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-20 14:57:45
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-20 15:01:37
class Solution:
	def defangIPaddr(self, address: str) -> str:
		return(address.replace('.','[.]'))

addr = "1.1.1.1"
solution = Solution()
print(solution.defangIPaddr(addr))