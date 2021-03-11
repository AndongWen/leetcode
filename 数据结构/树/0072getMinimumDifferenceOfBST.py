'''530二叉搜索树的最小绝对差：
	给定一个所有节点为非负值的二叉搜索树，求树中任意两节点的差的绝对值的最小值。'''

'''利用BST中序遍历有序，进行计算'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.prenode = None
        self.min = float('inf')
        
    def getMinimumDifference(self, root: TreeNode) -> int:
#		 遍历BST，形成数组，再遍历一次
#        self.ans = []
#        self.bns = float('inf')
#        self.inordertravell(root)
#        for i in range(len(self.ans)-1):
#            self.bns = abs(self.ans[i] - self.ans[i+1]) if abs(self.ans[i] - self.ans[i+1]) < self.bns else self.bns
#        return self.bns
#        
#        
#        
#    def inordertravell(self, root):
#        if not root:
#            return 
#        self.inordertravell(root.left)
#        self.ans.append(root.val)
#        self.inordertravell(root.right)
        
#   利用中序遍历得有序性，在遍历过程中直接求值
        self.inordertravell(root)
        return self.min
    
    def inordertravell(self, root):
        if not root:
            return 
        self.inordertravell(root.left)
        if self.prenode:
            self.min = min(self.min, root.val - self.prenode.val)
        self.prenode = root
        self.inordertravell(root.right)
        
