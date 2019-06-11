'''392判断子序列：给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）'''
'''思路：
	按照次序依次比对s中的元素是否在t中存在：双指针
	对t依次取切片，判断s中每个元素是否在其中出现'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
		'''思路1，效率低'''
        i, j =0 ,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def isSubsequence2(self, s: str, t: str) -> bool:
		'''思路2'''
        idx = 0
        for i in range(len(s)):
            tmp = t[idx:].find(s[i]) # 此tmp为切片t[idx:]中的索引
            if tmp == -1:
                return False
            idx = idx + tmp + 1 # 新切片的索引应该是旧切片索引+tmp+1
        return True
             
