'''34在排序数组中查找元素第一个和最后一个位置:
	给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]'''
'''h的取值，关乎选择的区间的右边到底是不是闭合的,同时也决定了循环的
条件和退出时l与h的关系'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = self.searchLeft(nums, target)
        right = self.searchRight(nums, target)
        return [left, right]
    
    def searchLeft(self, nums, target):
        l, h = 0, len(nums) 
        while l < h:
            m = l + (h-l)//2
            if nums[m] == target:
                h = m
            elif nums[m] > target:
                h = m
            elif nums[m] < target:
                l = m + 1
                
        if l == len(nums):
            return -1
        return l if nums[l] == target else -1
    
    def searchRight(self, nums, target):
        l, h = 0, len(nums)
        while l < h:
            m = l + (h-l)//2
            if nums[m] == target:
                l = m + 1
            elif nums[m] > target:
                h = m
            elif nums[m] < target:
                l = m + 1
        if h == 0:
            return -1
        return h-1 if nums[h-1] == target else -1
