273selfSquares(Medium)

Leetcode / 力扣

题目描述：For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9. = self.record[i-1] + nums[i]

# 动态规划
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

# 递归 贪心地去枚举组成这个数的最小组合，从1开始计算对应的组合数，以保证组合数最小
class Solution:
	def numSquares(self, n: int) -> int:
        def is_divide_by(n, count):
            if count == 1:
                return n in numsquares
            
            for k in numsquares:
                if is_divide_by(n-k, count-1):
                    return True
            return False

        numsquares = []
        for i in range(int(n**0.5)+1):
            numsquares.append(i**2)

        for j in range(1, n+1):
            if is_divide_by(n, j):
                return j

# 和上述解法一致，使用贪心BFS
class Solution:
    def numSquares(self, n: int) -> int:
        queue = [n]
        level =  0
        numsquares = [i*i for i in range(1, int(n**0.5)+1)]

        while queue:
            level += 1
            next_queue = set() # 避免重复的元素，节省空间和时间
            for remain in queue:
                for numsquare in numsquares:
                    if remain == numsquare:
                        return level
                    elif remain > numsquare:
                        next_queue.add(remain - numsquare)
                    else:
                        break

            queue = next_queue
