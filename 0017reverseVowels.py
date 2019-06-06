'''问题描述：编写一个函数，以字符串作为输入，反转该字符串中的元音字母。'''
class Solution:
	'''Python中字符串是不可变的，所以有两种解决方案：
		1.重新使用一个与源字符串长度一致的列表，最后转换成字符串
		2.直接将原先的字符串转换成列表'''
    def reverseVowels(self, s: str) -> str:
		'''代价大，重新创建一个列表，其中的值每次都要修改'''
        i = 0
        j = len(s)-1
        res = [0] * len(s)
        alist = ['a','e','i','o','u','A','E','I','O','U']
        while i <= j:
            if s[i] not in alist:
                res[i] = s[i]
                i += 1
            elif s[j] not in alist:
                res[j] = s[j]
                j -= 1
            else:
                res[i] = s[j]
                res[j] = s[i]
                i += 1
                j -= 1
        return ''.join(res)


    def reverseVowels2(self, s: str) -> str:
        vow = 'aeiouAEIOU'
        S = list(s)
        l, r = 0, len(s)-1
        while l<=r:
            while l<=r and S[l] not in vow:
                l += 1
            while l<=r and S[r] not in vow:
                r -= 1
            if l > r: break
            S[l], S[r] = S[r], S[l]
            l += 1
            r -= 1
        return ''.join(S)
