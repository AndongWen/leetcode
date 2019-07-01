'''565.数组嵌套
	索引从0开始长度为N的数组A，包含0到N - 1的所有整数。找到并返回最大的集合S，S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }且遵守以下的规则。

假设选择索引为i的元素A[i]为S的第一个元素，S的下一个元素应该是A[A[i]]，之后是A[A[A[i]]]... 以此类推，不断添加直到S出现重复的元素。'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
		'''任何一个已经被标记的点，从这个位置开始的数组长度一定小于经过这个点的那个数组，所以只要遍历一次'''
        res = float('-inf')
        for i in range(len(nums)):
            cnt = 0
            j = i
            while nums[j] != -1:
                t = j
                j = nums[j]
                nums[t] = -1 # 标记
                cnt += 1
            res = max(res, cnt)
         
        return res
