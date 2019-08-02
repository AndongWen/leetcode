'''241为运算表达式设计优先级:
	给定一个含有数字和运算符的字符串，为表达式添加括号，
	改变其运算优先级以求出不同的结果。你需要给出所有可能的组合的结果。
	有效的运算符号包含 +, - 以及 * 。'''
'''思路:分治，利用分隔符将表达式分成两个部分分别计算，
	两个for循环考虑所有的结果'''
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        ways = []
        if "+" not in input and "-" not in input and "*" not in input:
            ways.append(int(input))
            return ways
        for i in range(len(input)):
            if input[i] in {'+', '-', '*'}:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                for l in left:
                    for r in right:
                        if input[i] == "+":
                            ways.append(l+r)
                        elif input[i] == "-":
                            ways.append(l-r)
                        elif input[i] == "*":
                            ways.append(l*r)
        return ways
