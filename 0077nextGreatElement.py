'''503下一个更大元素:
	给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），
输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组遍历顺序，
这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。
如果不存在，则输出 -1。'''

'''思路：和温度那题类似，只是这里变成了循环数组。取余数即可'''
class Solution(object):
	def nextGreatElement(self, nums:list(int)) -> list(nums)
		if not nums:
			return nums
		n = len(nums)
		res = [-1]*n
		stack = []
		for i in range(2*n):
			k = i%n
			while stack and nums[stack[-1]] < nums[k]:
				j = stack.pop()
				res[j] = nums[k]
			if i < n:
				stack.append(i)
		return res

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        n = len(nums)
        res = [-1]*n
        max_index = nums.index(max(nums))
        stack = []
        for i in range(max_index, max_index-n, -1):
            while stack and stack[-1] <= nums[i]: #　必须有＝，以保证栈顶元素大于目前遍历元素
                stack.pop()
            if stack:
                res[i] = stack[-1]
            stack.append(nums[i])
        return res
