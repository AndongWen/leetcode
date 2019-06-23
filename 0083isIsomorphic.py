'''205同构字符串:给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
		# 直接利用题目中的定义
        if len(s) != len(t):
            return False
        hashmap = {}
        for i in range(len(s)):
            if s[i] not in hashmap:
                hashmap[s[i]] = t[i]
            else:
                if hashmap[s[i]] != t[i]:
                    return False
        return len(set(hashmap.keys())) == len(set(hashmap.values())) 

    def isIsomorphic(self, s: str, t: str) -> bool:
		# 两个字符串中每个位置上的字符在本字符串上第一次出现的索引一致时，他们同构
		return list(map(s.index, s)) == list(map(t.index, t))
		# map()它接收一个函数f和一个可迭代对象，并通过把函数f依次作用在list的每个
		# 元素上，得到一个新的可迭代对象 并返回。

