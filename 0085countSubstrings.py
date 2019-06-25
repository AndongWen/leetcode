'''647计算回文子串的数目:
	给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被计为是不同的子串。'''

'''0084题目的变体'''
class Solution:
	#　暴力解法
    def countSubstrings(self, s: str) -> int:
        cnt = 0
        if not s:
            return 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    cnt += 1
        return cnt

class Solution:
	# 中心扩散法
    def __init__(self):
        self.cnt = 0
        
    def countSubstrings(self, s: str) -> int:
        if not s:
            return 0
        for i in range(len(s)):
            self.helper(s, i, i+1)
            self.helper(s, i, i)
        return self.cnt
        
    def helper(self, s, start, end):
        l = start
        r = end
        while l >= 0 and r < len(s) and s[l] == s[r]:
            self.cnt += 1
            l -= 1
            r += 1

class Solution:
    def countSubstrings(self, s: str) -> int:
		# 动态规划
        n = len(s)
        cnt = n
        if n <= 1:
            return n
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i): # j取不到i，所以会漏掉自身这个字符，所以在cnt初始化得时候就设置了cnt = n
                if s[i] == s[j] and (dp[j+1][i-1] or i-j<=2):
                    dp[j][i] = True
                    cnt += 1
        return cnt
