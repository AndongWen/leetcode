'''以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。

在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径

请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。'''

class Solution(object):
    def simplifyPath(self, path: str) -> str:
        stack = [] # python中栈就是用列表封装的
        path  = path.split('/') # 将其所有的/删除用空字符串替代，返回值为列表
        for i in path:
            if i == '..':
                if stack: # 这两个条件必须分开写，不然会出错，eg:'/../'
                    stack.pop()
            elif i and i != '.':
                stack.append(i)
        return '/'+'/'.join(stack)

	def simplifyPath1(self, path: str) -> str:
		stack = []
		for i in path.split('/'):
			if i not in ['', '.', '..']:
				stack.append(i)
			elif i == '..':
				if stack:
					stack.pop()
			return '/'+'/'.join(stack)
