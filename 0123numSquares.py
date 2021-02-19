273selfSquares(Medium)

Leetcode / 力扣

题目描述：For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9. = self.record[i-1] + nums[i]

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            j = 1
            dp[i] = i
            while j * j <= i:
                dp[i] = min(dp[i], dp[i-j*j]+1)
                j += 1
        
        return dp[n]
