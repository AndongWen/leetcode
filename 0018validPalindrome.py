'''问题描述:给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。'''
'''回文字符串就是正读与反读完全一致'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
		'''利用回文字符串的性质'''
        r = s[::-1]
        if r == s:
            return True
        for i in range(len(s)):
            if s[i] != r[i]:
                m = s[:i] + s[i+1:] # 除去第i个元素
                if m != m[::-1]:
                    n = r[:i] + r[i+1:] # 除去第i+1个元素
                    return n == n[::-1]
                else:
                    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i <= j:
            if s[i] != s[j]:
                return self.ispalindrome(s, i, j-1) or self.ispalindrome(s, i+1, j)
            i += 1
            j -= 1
        return True
    
    def ispalindrome(self, s, i, j):
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
