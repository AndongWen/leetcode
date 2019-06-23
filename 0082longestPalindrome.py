'''409最长回文串:
	给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。'''

'''思路：统计每个字符串出现的次数，偶数直接加到最后的结果中，奇数则减１后加入，
	一旦有奇数出现，最后的结果可以在加上１，因为中间可以出现一个单独的字符串'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        flag = False
        cnt = coll.Counter(s)
        res = 0
        for k, v in cnt.items():
            if v % 2 == 0: # 偶数
                res += v
            else:
                res += v-1
                flag = True
        return res+1 if flag else res

'''还可以用一个长度为256的列表来作为哈希表来进行统计'''
