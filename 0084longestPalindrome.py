'''5最长回文子串：
	给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。'''

class Solution:
	# 暴力解法 依次对每个位置进行尝试 一共n(n+1)/2个子串，每次验证要o(n)的时间
	# 一共O(n*3)的时间复杂度
    def __init__(self):
        self.i = 0
        self.j = 0
      
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        longest = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i:j+1] == s[i:j+1][::-1] and longest < j-i+1:
				# s[i:j] j取不到
                    longest = j-i+1
                    self.i = i
                    self.j = j+1
           
        return s[self.i: self.j]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 中心扩展法 一共有2n-1个中心 每次搜索用掉O(n)得时间，总的复杂度为O(n*2)
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.helper(s, i, i) # 奇数
            len2 = self.helper(s, i, i+1) # 偶数
            max_len = max(len1, len2)
            if max_len > end - start: 
                start = i - (max_len-1)//2 
                end = i + max_len//2
        return s[start: end+1] # 后端的索引取不到
        
    def helper(self, s, start, end):
        l = start
        r = end
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r-l-1 # r与l都比符合条件得大1和小1 完美包括两种情况

class Solution:
    def longestPalindrome(self, s: str) -> str:
		'''动态规划：类似中心扩展的逆思考
		   dp 为一个二维数组，dp[j][i]表示s[j,i]能否形成回文串,如果dp[j][i]可以形成回
		   回文串，那么dp[j+1][i-1]也一定可以形成回文串；反过来，如果dp[j+1][i-1]可以
　　　　　 形成回文串，只需要对比s[j]与s[i]既可以判断s[j,i]是否为回文串.
		　 注意：
		        1.s[j+1,i-1]要存在，即i-1>j+1 ==> i-j>2
			    2.若不满足上述条件，则说明两者重合为一个字符，只要验证是s[i]与s[j]
				3.要形成字符串，必须要有i>j,所有二维数组中只有下三角形有用	
		　 动态转移方程为:dp[j][i] = (s[i] == s[j] and (i-j<=2 or dp[j+1][i-1]))'''
		n = len(s)
		if n <= 1:
			return s
		length = 1 # 至少长度为１
		res = s[0]
		
		dp = [[False for _ in range(n)] for _ in range(n)] # 初始化
		for i in range(n):
			for j in range(i):
				if s[i] = s[j] and (i-j<=2 or dp[j+1][i-1]):
					dp[j][i] = True
					if i-j+1 > length:
						length = i-j+1
						res = s[j: i+1]
		return res
