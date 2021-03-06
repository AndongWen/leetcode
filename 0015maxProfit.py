'''问题：给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易
（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
'''

class Solution(object):
	def maxProfit(self, prices:list) ->int:
		'''第一天买入第二天就可以卖
		在这种情况下，我们可以简单地继续在斜坡上爬升并持续增加从
连续交易中获得的利润，而不是在谷之后寻找每个峰值。最后，
我们将有效地使用峰值和谷值，但我们不需要跟踪峰值和谷值对应的成本
以及最大利润，但我们可以直接继续增加加数组的连续数字之间的差值，
如果第二个数字大于第一个数字，我们获得的总和将是最大利润。
这种方法将简化解决方案(建议画图）'''
		return sum(a-b for a, b in zip(prices[1:], prices) if a>b)
		# zip :从参数中的多个迭代器取元素组成一个新的迭代器
		#      返回一个zip对象，内部元素为元祖
		#      元素数目取决于迭代器中少的元素个数
