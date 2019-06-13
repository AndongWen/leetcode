'''104二叉树的最大深度'''
'''思路：一棵树要么是空树，要么有两个指针，每个指针指向一棵树。树是一种递归结构，很多树的问题可以使用递归来处理。'''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        rightdepth = self.maxDepth(root.right)+1
        leftdepth = self.maxDepth(root.left)+1
        return max(leftdepth, rightdepth)


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
		'''利用DFS遍历，迭代解法'''
        if not root:
            return 0
        stack = [] # 用列表做栈
        stack.append((root, 1))
        maxdepth = 0
        while stack:
            cur = stack.pop()
            curdepth = cur[1]
            maxdepth = max(curdepth, maxdepth)
            if cur[0].left:
                stack.append((cur[0].left, curdepth+1))
            if cur[0].right:
                stack.append((cur[0].right, curdepth+1))
        return maxdepth
