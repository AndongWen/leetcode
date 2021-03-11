413数组Ａ 包含 N 个数，且索引从0开始。
数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。

# 解法１：暴力解法，依次从头遍历
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        count = 0
        for i in range(len(A)-2):
            d = A[i+1] - A[i]
            for j in range(i+2, len(A)):
                if A[j] - A[j-1] == d:
                    count += 1
                else:
                    break
        return count

# 解法２：动态规划
# dp[i]表示以第i个索引结尾的等差数列的数组个数
class Solution:
	def numberOfArithmeticSlices(self, A):
		res = 0
		dp = [0] * len(A)
		for i in range(2, len(A)):
			if A[i]-A[i-1] == A[i-1]-A[i-2]:
				dp[i] = dp[i-1]+1
				res += dp[i]
		return res
