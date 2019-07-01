'''给定一个非空且只包含非负数的整数数组 nums, 数组的度的定义是指数组里任一元素出现频数的最大值。

你的任务是找到与 nums 拥有相同大小的度的最短连续子数组，返回其长度。
'''
import collections as coll

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        numcnt = coll.Counter(nums)
        maxcnt = numcnt.most_common(1)[0][1] # most_common返回的是元素为元组的列表
        res = float('inf')
        numfirstindex = {}
        numlastindex = {}
        for i in range(len(nums)):
            numlastindex[nums[i]] = i
            if nums[i] not in numfirstindex.keys():
                numfirstindex[nums[i]] = i
        
        for k in numcnt.keys():
            if numcnt[k] != maxcnt:
                continue
            cur = numlastindex[k] - numfirstindex[k] + 1
            res = min(res, cur)
         
        return res
