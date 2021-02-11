给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。

实现 NumArray 类：

NumArray(int[] nums) 使用数组 nums 初始化对象
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）

class NumArray:
	"""暴力解法"""
    def __init__(self, nums: List[int]):
    	self.data = nums
 
    def sumRange(self, i: int, j: int) -> int:
		sum_res = 0
		for i in range(i, j+1):
			sum_res += self.data[i]
		return sum_res
			

class NumArray:
	"""设置缓存解法"""
    def __init__(self, nums: List[int]):
        self.record = list(nums)
        for i in range(len(nums)):
            if i == 0:
                self.record[i] = nums[i]
            else:
                self.record[i] = self.record[i-1] + nums[i]
                
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.record[j]
        return self.record[j] - self.record[i-1]
