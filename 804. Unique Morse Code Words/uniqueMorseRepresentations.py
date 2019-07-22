# -*- coding: utf-8 -*-
# @Author: lujianhong
# @Date:   2019-07-22 14:24:41
# @Last Modified by:   lujianhong
# @Last Modified time: 2019-07-22 14:44:00
class Solution:
	def uniqueMorseRepresentations(self, words):
		i = 0
		mapped = dict()
		res = list()
		alphas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
		morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
		while i < len(alphas):
			mapped[alphas[i]] = morse[i]
			i = i + 1
		for word in words:
			temp = ""
			tolist = list(word)
			for alpha in tolist:
				temp += mapped[alpha]
			if temp not in res:
				res.append(temp)
			else:
				continue
		return len(res)


words = ["gin", "zen", "gig", "msg"]
solution = Solution()
print(solution.uniqueMorseRepresentations(words))