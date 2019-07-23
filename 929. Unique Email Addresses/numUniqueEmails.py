# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-23 15:46:01
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-23 16:14:09
class Solution:
	def numUniqueEmails(self, emails):
		res = []
		for email in emails:
			i = 0
			lst = list(email)
			pos = lst.index('@')
			lst1 = []
			try:
				pos1 = lst.index('+')
				while i < len(lst):
					if i >= pos1 and i < pos:
						i = i + 1
					else:
						lst1.append(lst[i])
						i = i + 1
			
			except:
				lst1 = lst
			j = 0
			while j < lst1.index('@'):
				if lst1[j] == '.':
					lst1.pop(j)
				else:
					j = j + 1
			result = "".join(lst1)
			if result in res:
				continue
			else:
				res.append(result)
		return len(res)


solution = Solution()
print(solution.numUniqueEmails(["testemail@leetcode.com","testemail1@leetcode.com","testemail+david@lee.tcode.com"]))
