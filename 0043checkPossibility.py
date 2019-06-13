'''665给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]'''
'''思路：
		设置一个标记量，遍历这个数组，当发现nums[i]<nums[i-1]，标记量就+1，
		同时修改这个数组，问题在于修改哪一个？？？
		如果直接修改nums[i]，将其变成多少？为了尽可能地不影响后面的元素，
		只能将其修改成nums[i-1]，但实际还是让nums[i]变大，很可能会影响到
		后面的元素
		所以应该将nums[i-1]修改成nums[i]
		但是需要注意如果nums[i-2]>nums[i],这种操作就不符合题意,还是要按照
		上面的来修改'''
class Solution(object)；
	def checkPossibility(self, nums: List[int]) -> bool:
		count = 0
		if len(nums) <= 2:
			return True
		for i in range(1, len(nums)):
			if nums[i] >= nums[i-1]:
				continue
			count += 1
			if count > 1:
				return False
#			[4,2,3]此种情况会出问题,他会将第二个元素变为4
#			说白了一般性情况最后写,特殊情况单独写
#			if i>=2 and nums[i] >= nums[i-2]:
#				nums[i-1] = nums[i]
#			else:
#				nums[i] = nums[i-1]
			if i >= 2 and nums[i] < nums[i-2]:
				nums[i] = nums[i-1]
			else: # 一般性的修改
				nums[i-1] = nums[i]	
		return count <= 1
