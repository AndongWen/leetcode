'''763.划分字母区间：字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一个字母只会出现在其中的一个片段。返回一个表示每个字符串片段的长度的列表。
输入: S = "ababcbacadefegdehijhklij"
输出: [9,7,8]
解释:
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。'''
'''思路：
		找到每个英文字母在字符串出现的最后位置，然后从第一个字符到此字符最后
		一次出现的区间内遍历，比较其中的字符最后一次出现的索引与区间的末尾，
		若更大则修改区间的末尾，直到遍历完这个区间，对应的长度就是末尾-头部+
		1，之后遍历的位置就是末尾+1处。'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
	'''用字典保存每个英文字母在字符串出现的最后位置，需要遍历一次'''
		if not S:
			return []
		res = []
		d = {}
	 	for i in range(len(S)):
			d[S[i]] = i
		start = 0
		end = d[S[start]]
		while end < len(S):
			i = start
			while i < end:
				if end < d[S[i]]:
					end = d[S[i]]
				i += 1
			res.append(end-start+1)
			if end >= len(S)-1:
				return res
			start = end+1
			end = d[S[start]]
		return res	
