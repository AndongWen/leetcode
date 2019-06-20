'''235二叉树的最近公共祖先：给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一
个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
'''

'''思路：利用二叉搜索树的节点数值特性'''
class Solution(object):
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#        递归
#        if (p.val-root.val) * (q.val-root.val) <= 0:
#            return root
#        if p.val > root.val and q.val > root.val:
#            return self.lowestCommonAncestor(root.right, p, q)
#        if p.val < root.val and q.val < root.val:
#            return self.lowestCommonAncestor(root.left, p, q)

#		迭代
        if q.val > p.val:
            q, p = p, q
        while True:
            if root.val > p.val:
                root = root.left
            elif root.val < q.val:
                root = root.right
            else:
                return root
