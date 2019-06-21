'''653.两数之和-BST
	给定一个二叉搜索树和一个目标结果，如果 BST 中存在两个元素且它们的和等于给定
的目标结果，则返回 true。'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections as coll

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
		# 中序遍历后，用双指针解决问题
        self.ans = []
        self.inordertravell(root)
        q, p = 0, len(self.ans)-1
        while q < p:
            if self.ans[q] + self.ans[p] == k:
                return True
            elif self.ans[q] + self.ans[p] > k:
                p -= 1
            else:
                q += 1
        return False
        
        
    def inordertravell(self, root: TreeNode):
        if not root:
            return 
        self.inordertravell(root.left)
        self.ans.append(root.val)
        self.inordertravell(root.right)
        


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.hashmap = {}
        self.ret = False
        def check(left, right):
            if not self.ret and left:
                # print('L', self.hashmap, left.val, k - left.val)
                if (k - left.val) in self.hashmap:
                    # print('L=======')
                    self.ret = True
                else:
                    self.hashmap[left.val] = 1
                    check(left.left, left.right)
            if not self.ret and right:
                # print('R', self.hashmap, right.val, k - right.val)
                if (k - right.val) in self.hashmap:
                    # print('R========')
                    self.ret = True
                else:
                    self.hashmap[right.val] = 1
                    check(right.left, right.right)
        
        self.hashmap[root.val] = 1
        check(root.left, root.right)
        return self.ret
