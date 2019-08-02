'''34在排序数组中查找元素的第一个和最后一个位置:
	给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
		# 不符合算法复杂度
        for i in range(len(nums)):
            if nums[i] == target:
                left = i
                break
        else: # 当for循环被break中断后，其后的else语句就不执行了
            return [-1, -1]
          
        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right = j
                break
              
        return [left, right]
