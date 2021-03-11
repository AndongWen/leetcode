'''637.二叉树的平均值:给定一个非空二叉树, 返回一个由每层节点平均值组成的数组.'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections as coll

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
		'''先层次遍历，在求平均值'''
        res = []
        if not root:
            return 0
        q = coll.deque()
        q.append((root, 0))
        level = 0
        while q:
            node, cur = q.popleft()
            if level == cur:
                if level != 0:
                    res.append(levelres)
                levelres =[]
                level += 1
            levelres.append(node.val)
			if node.left:
				q.append((node.left, cur+1))
			if node.right:
				q.append((node.right, cur+1))
            
        lastres =[]
        for temp in res:
            sum = 0
            for i in range(len(temp)):
                sum += temp[i]
            lastres.append(sum/len(temp))
        return lastres

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
		'''遍历过程直接算'''
        res = [] 
        if not root:
            return res
        q = coll.deque()
        q.append(root)
        while q:
            n = len(q)
            sum = 0
            for i in range(n):
                node = q.popleft()
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum/n)
        
