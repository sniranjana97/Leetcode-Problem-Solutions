class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		result = list()
		best = list()
		if len(s) == 1:
			return 1
		for num,i in enumerate(s):
			if i in result:
				index = result.index(i)
				result = result[index+1:]
			result.append(i)
			if len(best) < len(result):
				best = list(result)
		return len(best)
