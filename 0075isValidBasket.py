'''20有效的括号：
	给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if not s:
            return True
        i = 0
        while i < len(s):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                j = stack.pop()
                if j == '(' and (s[i] == '}' or s[i] == ']'):
                    return False
                elif j == '[' and (s[i] == '}' or s[i] == ')'):
                    return False
                elif j == '{' and (s[i] == ')' or s[i] == ']'):
                    return False
            i += 1    
        if stack:
            return False
        return True


class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', ']':'[', '}':'{'}
        stack = []
        for char in s:
            if char in d:
                j = stack.pop() if stack else '&'
                if j != d[char]:
                    return False
            else:
                stack.append(char)
        return not stack
