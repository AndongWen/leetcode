'''451给定一个字符串，请将字符串里的字符按照出现的频率降序排列。
	同种频率的字符串没有先后顺序
	和 347很类似'''
class Solution:
    def frequencySort(self, s: str) -> str:
		'''内置方法'''
        res = ''
        a = collections.Counter(s).most_common()
        for k, v in a:
            res += k*v
        return res

    def frequencySort2(self, s: str) -> str:
		'''非内置方法：重点是sorted排序'''
        res = ''
        d = {}
        for i in s:
            d[i] = d.get(i, 0) + 1
        c = sorted(d.keys(), key = d.get, reverse = True)
        for i in c:
            res += d[i]*i
        return res
