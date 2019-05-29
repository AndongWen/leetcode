'''给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。'''
class Solution:
	# 不是最优解
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        i, j = 0, 0 # 滑动窗口的左右的下表
        res = []
        n = len(s)
        while i < n and j < n :
            if s[j] not in res:
                res.append(s[j])
                j += 1
                if j-i> max_len:
                    max_len = j-i
            else:
                res.remove(s[i])
                i += 1
        return max_len
