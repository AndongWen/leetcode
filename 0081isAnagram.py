'''242有效的字母易位词：
	给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。'''

'''思路：哈希表 -->字典　s让其值增加，t让其值减少，最后看所有的值是否都为0
			也可以使用collections.Counter
		列表：由于都是小写字母，所以可以使用长度为26的列表完成任务'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0] * 26
        for char in s:
            res[ord(char)-97] += 1 # ord() 函数是 chr() 函数（对于 8 位的 ASCII 字符串）的配对函数，它以一个字符串（Unicode 字符）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值。
        for char in t:
            res[ord(char)-97] -= 1
        for i in range(26):
            if res[i] != 0:
                return False
        return True

    def isAnagram(self, s: str, t: str) -> bool:
        return coll.Counter(s) == coll.Counter(t)
