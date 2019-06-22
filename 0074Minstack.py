'''155最小栈：设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素'''

'''思路:使用辅助栈'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] 
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]: # 此处等号不可以省去
            self.min_stack.append(x)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return "error"
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return "error"
        return self.stack[-1]
         
    def getMin(self) -> int:
        if not self.stack:
            return "error"
        return self.min_stack[-1]
