'''198打家劫舍1：你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。'''
'''思路：动态规划：
		依照提议，小偷来偷第n家的时候，他只能来自第n-2家或者第n-3家（间隔只能是1或2，超过2其实中
	    间的也可以偷），所以就可以递推出偷第n家的最大值，最后返回所得值就好'''
class Solution(object):
	def rob(self, nums: List) -> int:
		if not nums:
			return 0
		n = len(nums)
		if n <= 2:
			return max(nums)
		money = [nums[0]]+[nums[1]]+[nums[0]+nums[2]] + [0]*(n-3) # 初始化money列表
		for i in range(3, n):
			money[i] = max(money[i-2]+nums[i], money[i-3]+nums[i])
		return max(money)

'''思路：动态规划：
		依照提议，每次记录当前最大收益，他是前一家的最大收益与前前一家加上当前家收益的最大值（
		前前前加当前包括在后者之中，利用状态转义方程：dp[i] = max(dp[i-1],dp[i-2]+nums[i])'''

class Solution(object):
	def rob(self, nums: List) -> int:
		if not nums:
			return 0
		n = len(nums)
		if n <= 2:
			return max(nums)
		q, p = nums[0], max(nums[0], nums[1]) # q, p分别记录第i-2和第i-1的最大收入
		for i in range(2, n):
			next_ = max(p, q+nums[i])
			q, p = p, next_
		return p


class Solution:
    def rob(self, nums: List[int]) -> int:
		'''奇偶数组合加上复制对方最优解'''
        sumodd = 0
        sumeven = 0
        n = len(nums)
        for i in range(n):
            if i%2 == 1:
                sumodd += nums[i]
                sumodd = max(sumodd, sumeven)
            else:
                sumeven += nums[i]
                sumeven = max(sumeven, sumodd)
        return max(sumodd, sumeven)
