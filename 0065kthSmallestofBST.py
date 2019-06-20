'''230.二叉搜索树中的第K个最小的元素：给定一个二叉搜索树，编写一个函数 
   kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。'''

'''思路:利用二叉搜索树的特点，跟节点大于左孩子，小于右孩子
		用中序遍历得到的节点数值，正好是升序的'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections as coll

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        q = coll.deque()
        q.append(root)
        cur  = root
        cnt = 0
        
        while cur or q:
            while cur:
                q.append(cur)
                cur = cur.left
            cur = q.pop()
            cnt += 1
            if cnt == k:
                return cur.val
            cur = cur.right


    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def gen(r):
            if r is not None:
                yield from gen(r.left)
                yield r.val
                yield from gen(r.right)
        
        it = gen(root)
        for _ in range(k):
            ans = next(it)
        return ans
        
