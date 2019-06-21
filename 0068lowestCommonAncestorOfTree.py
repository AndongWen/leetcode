'''236二叉树的最近公共祖先：
	给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先)'''

'''思路：递归：
			使用三个标记变量来对应一个节点的本身、左子树和右子树是否找到对应的节点
			当其中有两个标记量被改动，说明已经找到了最近的公共祖先'''

import collections as coll

class Solution(object):
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		'''递归'''
		self.ans  = None # 存储最后的最近公共祖先

		def helper(root: 'TreeNode'):
			if not root:
				return False
			left = helper(root.left)
			right = helper(root.right)
			mid = 1 if root.val == p.val or root.val == q.val else 0

			if left+right+mid >= 2:
				self.ans = root
		
			return left or right or mid

		helper(root)
		return self.ans


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		'''递归'''
		        if not root or root.val == q.val or root.val == p.val:
            return root
		# 从本质上讲left与right是标记量
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        elif not left and not right:
            return None
        elif left:
            return left
        elif right:
            return right

    def lowestCommonAncestor3(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
		'''迭代(父亲指针)：BFS遍历直到找到p与q，用字典保存途中遇到所有节点的父亲节点，
			然后找到q的所有祖先组成一个集合，依次迭代p的祖先，直到p的某个祖先第一次
			出现在集合中
			此时，在字典中，所有节点都指向了根节点，可以将二叉树理解为一个所有节点都
			指向根节点的链表，此时相当于求两个相交链表的交点'''

		parents = {root: None}
		stack = coll.deque()
		stack.append(root)

		while q not in parents or p not in parents:
			cur = stack.pop()
			if cur.left:
				parents[cur.left] = cur	
				stack.append(cur.left)
			if cur.right:
				parents[cur.right] = cur	
				stack.append(cur.right)

		ancestor = set()
		while q: # 将q所有祖先加入到集合中(包括q本身)
			ancestor.add(q)
			q = parents[q] # 不断地迭代q的祖先
		
		while p not in ancestor:
			p = parents[p]

		return p
