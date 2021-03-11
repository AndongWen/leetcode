'''问题描述:给定一个二叉树，返回它的前序 遍历。'''
class Solution(object):
	def preorderTravel(self, root:TreeNode) -> list[int]:
		'''递归解法'''
		if not root: # 节点为空
			return []
		res = []
		res.append(root.val)
		res += self.preorderTravel(root.left) # 列表拼接
		res += self.preorderTravel(root.right)
		
		return res


	def preorderTravel2(self, root:TreeNode) -> list[int]:
		'''迭代解法'''
		res, stack = [], []
		while root is not None or stack:
			while root:
				res.append(root.val)
				stack.append(root)
				root = root.left # 一直下行直到找到树中最左节点
			node = stack.pop() # 左节点在一定程度上说也是父节点
			root = node.right
		return res
