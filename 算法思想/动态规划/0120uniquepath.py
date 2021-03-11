62一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。 
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

解法一：动态规划，与119题目类似
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        a = [None] * n
        grid = [a for i in range(m)]
        grid[0][0] = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    grid[0][0] = 1
                elif i == 0:
                    grid[i][j] = grid[i][j-1]
                elif j == 0:
                    grid[i][j] = grid[i-1][j] 
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1] 
        return grid[-1][-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
		"""空间复杂度o(2n)"""
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j-1]
            pre = cur[:]
        return pre[-1]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
		"""空间复杂度ｏ(n)"""
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]


解法二：数学中的排列组合: 一共要走ｍ+n-2步，其中ｍ-1向下
class Solution:
	def uniquePaths(self, m: int, n: int) -> int:
		return int(math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)) 
