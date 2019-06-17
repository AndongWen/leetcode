'''404左子叶之和：返回一个二叉树所有左叶子节点数值之和'''
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
# 递归
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
