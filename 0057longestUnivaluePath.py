'''给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示'''

'''思路：这样的路径可以理解为从某个节点出发的两个箭头（其中箭头的长度可以为0），记录
这两个箭头总和的最大值，最后返回即可.这两个箭头正好为左右孩子。'''

class Solution(object):
	def longestUnivaluePath(self, root: TreeNode) -> int:
		'''递归'''
		self.ans = 0

		if not root:
			return 0
		self.helper(root)
		return self.ans

	def helper(self, root: TreeNode) -> int:
		if not root:
			return 0
		left = self.helper(root.left) # 计算左子树的最大箭头长度
		right = self.helper(root.right) # 计算右子树的最大箭头长度
		l_path = r_path = 0 # 如果下面两个条件都不符合，则次root为跟节点的长度为0
		# 判断当前的节点与其两个孩子的val是否相等
		if root.left and root.left.val == root.val:
			l_path = left+1
		if root.right and root.right.val == root.val:
			r_path = right+1
		self.ans = max(self.ans, l_path + r_path)
		return max(l_path, r_path) # 返回的是最大值,不是两者之和
