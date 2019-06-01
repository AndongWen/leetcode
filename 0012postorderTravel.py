'''问题描述:给定一个二叉树，返回它的前序 遍历。'''
class Solution(object):
	def postorderTravel(self, root:TreeNode) -> list[int]:
		'''递归解法'''
		if not root: # 节点为空
			return []
		res = []
		res += self.postorderTravel(root.left) # 列表拼接
		res += self.postorderTravel(root.right)
		res.append(root.val)
		
		return res


	def postorderTravel2(self, root:TreeNode) -> list[int]:
		'''迭代解法'''
		res, stack = [], []
		while root is not None or stack:
			while root:
				stack.append(root)
				root = root.left if root.left else root.right
				# 能左就左，否则右行	
			node = stack.pop()
			res.append(node.val)
			if stack and node == stack[-1].left: # node为栈顶节点的左孩子，进而转到右孩子
				root = stack[-1].right
			else: # 已经到整个树的根节点或者 node就是栈顶节点的右孩子
				t = None
		return res
