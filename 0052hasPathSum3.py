'''437路径总和3：给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。'''
'''思路：
		1.暴力解法：
			此总和可以时从任意一个非空的节点开始，所以可以用路径总和1来解决
			即总和可以从当前节点开始，也可以从两个孩子开始，即有两层递归
			也可以理解为每个节点做可以作为路劲总和1中解法的父节点，效率很低
		2.优化解法，通过dfs+回溯：
			记录从根节点到当前节点的和为cursum与其对用的频率，若cursum-sum 
			= oldsum之前记录过，说明这条路上，存在从某个节点到当前节点总和
			等于sum的。但是当累计的节点从一个节点的左孩子转向右孩子时，需要
			回溯。Python中可以使用字典来保存对应的记录'''
class Solution(object):
	'''思路一'''
	def haspathSum(self, root: TreeNode, sum: int) -> int:
		if not root:
			return 0
		res = self.haspathSumFromRoot(root, sum) + self.haspathSum(root.left, sum) + self.haspathSum(root.right, sum)
		return res

	def haspathSumFromRoot(self, root: TreeNode, sum: int) -> int:
		'''实际为上面的函数反复调用此函数'''
		if not root:
			return 0
		res = 0
		if sum == root.val:
			res += 1
		res += self.haspathSumFromRoot(root.left, sum-root.val)+self.haspathSumFromRoot(root.right, sum-root.val)
		return res	
