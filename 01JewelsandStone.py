'''问题描述：给定两个字符串J与S,判断J中所有字符在S中出现的次数（J中字符互异）'''

class Solution(object):
	def numJewelsInStone(self, J, S):
		count = 0
		for char in S:
			count += char in J
		return count


a = Solution()
res = a.numJewelsInStone('adsff','bbbbbbbbaa')
print(res)
