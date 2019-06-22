'''1.两数之和:给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
		'''先排序，后利用双指针，但在最后查找原先的索引时，注意索引可能相等的情况
			本质为数组中有元素相等'''
        if not nums:
            return nums
        num = sorted(nums)
        i, j = 0, len(nums)-1
        while i != j:
            if num[i] + num[j] == target:
                break
            elif num[i] + num[j] > target:
                j -= 1
            else:
                i += 1
        if i == j:
            return []
        a, b = nums.index(num[i]), nums.index(num[j])
        if a == b:
            nums.remove(num[j])
            b = nums.index(num[j]) + 1
        return [a,b] 
