'''101对称二叉树：判断一颗二叉树是不是镜像对称'''
'''思路1：递归：什么样的树是对称二叉树？两颗树的根节点数值一样，且任意一颗树的左孩子都和另一颗树
				的右孩子一样(判断类似与子树）'''

class Solution(object):
	def isSymmetric(self, root: TreeNode) -> bool:
		if not root:
			return True
		return self.issymmetric(root.left, root.right)

	def issymmetric(self, t1: TreeNode, t2: TreeNode) -> bool:
		if not t1 and not t2:
			return True
		if not t1 or not t2:
			return False
		if t1.val != t2.val:
			return False
		return self.issymmetric(t1.left, t2.right) and self.issymmetric(t1.right, t2.left) 

'''思路：使用迭代,则需要一个辅助栈或队列都可以
	 	 此处使用队列，每次弹出两个节点，正好一个是左孩子，一个是右孩子。
		 判断两者的关系，直到队列为空时则返回True'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections as coll

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = coll.deque()
        q.append(root.left)
        q.append(root.right)
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            if not node1 and not node2: # 都是空节点，说明到了某个根节点，不能直接说明 True
                continue
            if not node1 or not node2: # 一空一非空，一定为False
                return False
            if node1.val != node2.val: # 节点不等，说明一定False
                return False
			# 能顺利到达此处，说明两个节点的val相等
            q.append(node1.left)
            q.append(node2.right)
            q.append(node1.right)
            q.append(node2.left)
            
        return True	
