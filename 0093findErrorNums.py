'''645.集合 S 包含从1到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 nums 代表了集合 S 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。'''
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
		'''类似leetcode的一题，先将每个元素排到对应的位置，既可以找到题目所需元素,
			但超时'''
        for i in range(len(nums)):
            while nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return [nums[i], i+1]


    def findErrorNums(self, nums: List[int]) -> List[int]:
		'''用计数字典解决问题'''
		d = coll.Counter(nums)
        miss = []
        repeat = []
        for i in range(1,len(nums)+1):
            if d[i] == 2: # 此值不存在时，Counter中返回0
                repeat.append(i)
            elif d[i] == 0:
                miss.append(i)
                
        return repeat+miss

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
		'''纯数学方法'''
        repeat = sum(nums)- sum(set(nums))
        n = len(nums)
        miss = int(n*(n+1)/2 - sum(set(nums)))
        
        return [repeat, miss]
