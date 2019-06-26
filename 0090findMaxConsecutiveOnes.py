'''485给定一个二进制数组， 计算其中最大连续1的个数。'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_l = 0
        cur = 0
        for i in range(len(nums)):
            cur = 0 if nums[i] == 0 else cur + 1
            max_l = max(max_l, cur)
          
        return max_l
