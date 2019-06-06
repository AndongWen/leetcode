'''524问题描述：给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。'''
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
		'''双指针进行比较,利用新建立的列表进行记'''
        d.sort() # 不可以写 d = d.sort() 这样等价于把排序后d的地址引用给了d
        l1 = len(s)
        count = []
        long = 0
        for elem in d:
            l2 = len(elem)
            i, j = 0, 0
            while i < l1 and j < l2:
                if elem[j] == s[i]:
                    j += 1
				i += 1
            if j == l2:
                count.append(j)
                if j > long:
                    long = j
            else:
                count.append(0)
        return d[count.index(long)] if long > 0 else ''

class Solution:
	'''用一个字符串来保存索要的值，并不断的更新'''
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longestword = ''
        def islongest(s, t):
            i, j = 0, 0
            while i < len(s) and j <len(t):
                if s[i] == t[j]:
                    j += 1
                i += 1
            return j == len(t) 
        
        for word in d:
            l1 = len(longestword)
            l2 = len(word)
            if l1 > l2 or (l1 == l2 and longestword < word):
                continue
            if islongest(s, word):
                longestword = word
        return longestword
