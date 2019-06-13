'''110平衡二叉树：判断一棵树是不是平衡二叉树'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
		'''有太多的重复计算，时间复杂度O(n)'''
        if not root:
            return True
        return abs(self.depth(root.right)-self.depth(root.left))<=1 and self.isBalanced(root.right) and self.isBalanced(root.left)
    
    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.depth(root.right), self.depth(root.left))+1


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
		'''其中只要有一颗子树不是平衡二叉树，就可以停止计算高度了'''
        return self.depth(root) != -1
    
    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.depth(root.left)
        if left == -1:
            return -1
        right = self.depth(root.right)
        if right == -1:
            return -1
        return max(left, right)+1 if abs(left-right) <= 1 else -1
		
