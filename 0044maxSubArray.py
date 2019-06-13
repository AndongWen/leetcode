'''53最大子序和：给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和'''
'''思路：
		1.动态规划：用两个变量，一个记录当前的和，一个记录最大的和，当之前的
		和大于0，说明最大子序和可能还要继续；若小于等于0，说明当前最大子序和
		到此为止，新的序列从这个元素开始
		2.分而治之：最大子序和，这样的序列要么出现在左边，要么出现在右边，
		或者中间，因此可以使用递归，但是时间复杂度不及1'''
class Solution(object):
	def maxSubArray(self, nums):
		'''1'''
		pre = nums[0]
		max_ = nums[0]
		for i in range(1, len(nums)):
			pre = pre + nums[i] if pre > 0 else nums[i]
			max_ = max(max_, pre)
		return max_

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
		'''2'''
        if len(nums) == 1:
            return nums[0]
        else:
            max_left = self.maxSubArray(nums[0: len(nums)//2])
            max_right = self.maxSubArray(nums[len(nums)//2:])
        max1 = nums[len(nums)//2-1]
        temp1 = 0
        for i in range(len(nums)//2-1, -1, -1):
            temp1 += nums[i] 
            max1 = max(max1, temp1)
        
        max2 = nums[len(nums)//2]
        temp2 = 0
        for i in range(len(nums)//2, len(nums)):
            temp2 += nums[i] 
            max2 = max(max2, temp2)
        
        return max(max_left, max_right, max1+max2)
