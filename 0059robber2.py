'''213:你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都围成一圈，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。'''
'''思路：同1类似，只是分情况讨论'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 3:
            return max(nums)
        q1, p1 = nums[0], max(nums[0], nums[1])
        for i in range(2, n-1): # 不偷最后一家
            next_ = max(p1, q1+nums[i])
            q1, p1 = p1, next_
            
        q2, p2 = nums[1], max(nums[1], nums[2])
        for i in range(3, n): # 不偷第一家
            next_= max(p2, q2+nums[i])
            q2, p2 = p2, next_
            
        return max(p1, p2)
