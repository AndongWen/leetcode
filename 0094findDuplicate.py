'''287查找重复数:
	给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。'''

'''如果可以使用空间，用collections.Counter计数器即可'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 二分法查找
        l = 1
        r = len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            cnt = self.search(nums, mid) # 返回的是小于等于mid的个数
            if cnt <= mid: # 说明mid左侧没有重复的数字
                l = mid + 1
            else:
                r = mid - 1
        return l
        
    def search(self, nums, target):
        res = 0
        for i in range(len(nums)):
            if nums[i] <= target:
                res += 1
        return res

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 双指针解法，类似与链表中寻找环得入口
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return fast
