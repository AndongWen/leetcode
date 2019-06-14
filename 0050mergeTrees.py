'''617合并二叉树：给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。
'''
import collections as coll
'''先序遍历的变体'''

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		'''递归方法，利用递归法的三步'''
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    def mergeTrees2(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
		'''迭代'''
		if not (t1 and t2):
			return t1 or t2
		q1, q2 = coll.deque([t1]), coll.deque([t2])
		# 只要t2位置有节点，t1必须有，若无则需要补齐
		while q1 and q2:
			node1, node2 = q1.popleft(), q2.popleft() # 出队列
			if node1 and node2: # 进入循环的前提是，两者不为空
				node1.val += node2.val
				# 因为在t1的基础上合并，所以在node2左右孩子位置有节点时
				# node1必须也有,设置也很简单，就是补个TreeNode(0)
				# 当node2左右孩子为空时，不需要对node1进行改动，也不会进入这段代码
				if (not node1.left) and node2.left:
					node1.left = TreeNode(0)
				if (not node1.right) and node2.right:
					node1.right = TreeNode(0)
				q1.append(node1.left)
				q1.append(node1.right)
				q2.append(node2.left)
				q2.append(node2.right)
		return t1	
