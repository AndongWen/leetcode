'''669.修剪二叉搜索树:给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。
通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，
所以结果应当返回修剪好的二叉搜索树的新的根节点。'''

'''二叉搜索树：一个节点，如果有左孩子，则左孩子所有的值都不大于根节点的值，
						 如果有右孩子，则右孩子所有的值都不小于根节点的值
			将这颗树所有节点垂直投影到一个轴上，所有节点的值正好是升序'''
class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        if root.val > R:
            return self.trimBST(root.left, L, R)
        if root.val < L:
            return self.trimBST(root.right, L, R)
        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root
