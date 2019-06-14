'''226反转一颗二叉树'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        right = root.right # 之后的操作会改变root.right,故先保存
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(right)
        return root

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        queue = []
        queue.append(root)
        while queue:
            curnode = queue.pop(0)
            temp = curnode.right
            curnode.right = curnode.left
            curnode.left = temp
            if curnode.left:
                queue.append(curnode.left)
            if curnode.right:
                queue.append(curnode.right)
        return root
