'''问题描述：输入一个合法的括号字符串，将最外层的括号去除，返回内部的内容
	如输入：(())(())  输出为：()()
      输入  ()()()    输出为：""  '''
class Solution(object):
	def RemoveOuterParenthese(self,str):
		res = [] # 用于存储最外层括号内的元素
		left = 0 # 用于记录剩余的左括号数目，即未匹配完的括号数目
		for i in str:
			if i == '(':
				if left:
					res.append(i)
				left += 1
			elif i == ')':
				if left > 1:
					res.append(i)
					left -= 1
				elif left == 1:
					left -= 1
		return ''.join(res)

a = Solution()
b = a.RemoveOuterParenthese('()((()())())')
print(b)
					
