'''667给定两个整数 n 和 k，你需要实现一个数组，这个数组包含从 1 到 n 的 n 个不同整数，同时满足以下条件：

① 如果这个数组是 [a1, a2, a3, ... , an] ，那么数组 [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数；.

② 如果存在多种答案，你只需实现并返回其中任意一种.'''
'''思路:数学找规律的题目。
	将前k+1个数，按照 1, k+1, 2, k,......,k//2, k//2+1
	存放，这前k+1个数字正好构成了k的不同的整数，后面的值只要依次填入即
	可'''
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        nums = [1] * n
        a = k
        for i in range(1, k+1):
            nums[i] = nums[i-1]+a if i%2 == 1 else nums[i-1]-a
            a -= 1
        for i in range(k+1, n):
            nums[i] = i+1
        
        return nums
