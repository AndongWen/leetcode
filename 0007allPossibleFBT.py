'''问题描述：满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

返回包含 N 个结点的所有可能满二叉树的列表。
 答案的每个元素都是一个可能树的根结点。

答案中每个树的每个结点都必须有 node.val=0。

你可以按任何顺序返回树的最终列表。'''

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	dres = {0:[], 1:[TreeNode(0)]} # 用于存储一定节点数目的满二叉树情况，避免重复计算

	def allPossibleTree1(self, N):
		'''不足之处：左右节点的数目互换的时候，需要重新计算，即当
			有些节点数目构成二叉树的时候，对应的情况会反复计算'''
		if N == 1:
			return [TreeNode(0)] # 返回对应的根节点
		elif N%2 == 0:
			return []
		res = [] # 用于存储每个满二叉树的根节点，方便后续的遍历
		for i in range(1, N, 2): # 偶数不可能形成满二叉树
			for left in self.allPossibleTree(i):
				for right in self.allPossibleTree(N-i-1):
					node = TreeNode(0)
					node.left = left
					node.right = right
					res.append(node) # 每次加入一个根节点，知道最后返回整个二叉树的根节点，内嵌的res一旦调用结束便释放
		return res

	def allPossibleTree2(self, N):
		if N not in Solution.dres:
			if N%2 == 0:
				return []
			res = [] # 用于存储每个满二叉树的根节点，方便后续的遍历
			for i in range(1, N, 2): # 偶数不可能形成满二叉树
				for left in self.allPossibleTree(i):
					for right in self.allPossibleTree(N-i-1):
						node = TreeNode(0)
						node.left = left
						node.right = right
						res.append(node) # 每次加入一个根节点，知道最后返回整个二叉树的根节点，内嵌的res一旦调用结束便释放
			Solution.dres[N] = res
		return Solution.dres[N]
			
