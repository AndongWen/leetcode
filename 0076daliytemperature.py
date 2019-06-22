'''739每日温度:根据每日 气温 列表，请重新生成一个列表，对应位置的输入是你需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。'''

'''思路：维护一个递减的栈，对温度数组进行遍历，直到当前遍历到的数字大于栈顶的数字，将栈顶元素弹出
　　　　。由于res保存的是索引的差值，所以栈保存的是元素索引。'''
class Solution(object):
	def daliytemperature(self, T: list) -> list:
		res = [0] * len(T)
		stack = []
		for i in range(len(T)):
			while stack and T(i) > T(stack[-1]):
				j = stack.pop()
				res[j] = i - j
			stack.append(i)
		return res
