'''226反转一颗二叉树'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        right = root.right # 之后的操作会改变root.right,故先保存
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(right)
        return root
