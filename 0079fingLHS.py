'''594最长和谐子序列：
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。'''

'''哈希表'''
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        longest = 0
        if not nums:
            return 0
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        for key in hashmap.keys():
            if key+1 in hashmap:
                longest = max(longest, hashmap[key] + hashmap[key+1])
            
        return longest

'''排序后,用两个指针，类似窗口'''
