'''543二叉树的直径：给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。'''
'''思路:仔细观察可以得出，实际就是问同一个节点左右两棵树深度之和的最大值
    	就是树深度的变体'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        self.depth(root)
        return self.res
    
    def depth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        self.res = max(self.res, left+right)
        return max(left, right)+1
