'''121给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票'''
'''思路：1暴力解法：我们需要找出给定数组中两个数字之间的最大差值（即，最大利润）。此外，第二个数字（卖出价格）必须大于第一个数字（买入价格）。

形式上，对于每组 i 和 j（其中 j > i）我们需要找出 max(prices[j]−prices[i])
		 2一次遍历：只要记录前面的最小价格，将这个最小价格作为买入价格，然后将当前的价格作为售出价格，查看当前收益是不是最大收益。'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
		'''思路2'''
        maxprofit = 0
        if not prices:
            return 0
        minprices = prices[0]
        for i in range(len(prices)):
            if prices[i] < minprices:
                minprices = prices[i]
            else:
                maxprofit = max(maxprofit, prices[i]-minprices)
        return maxprofit
