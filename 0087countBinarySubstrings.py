'''696计数二进制子串：
	给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

重复出现的子串要计算它们出现的次数。
'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
		# last记录前一种数字连续出现的次数；　cur记录当前一种数字连续出现的次数
		# 当last >= cur　此时一定包含符合条件的子串
        last, cur = 0, 1
        cnt = 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                last = cur
                cur = 1
            if last >= cur:
                cnt += 1
                
        return cnt
