'''540有序数组中单一的元素:
	给定一个只包含整数的有序数组，每个元素都会出现两次，
	唯有一个数只会出现一次，找出这个数。
	您的方案应该在 O(log n)时间复杂度和 O(1)空间复杂度中运行。'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
		# 时间复杂度为O(n),不符合题目意思
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]
         
        return res

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
		'''根据时间复杂度，可以看出来要二分法解决问题
		index为该元素的位置索引。m为索引，当m+1<index且m为偶数时
		一定有nums[m] == nums[m+1],反之则不等。由此判断index所处的
		的区间'''
		l, h = 0, len(nums)-1
		while l < h:
			m = l + (h-l)//2
			if m&0x1:
				m -= 1 # 保证l,m,h都是偶数，是的查找区间为奇数
			if nums[m] == nums[m+1]:
				l = m + 2
			else:
				h = m
		return nums[l]
