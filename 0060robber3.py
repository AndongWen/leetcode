'''337.在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。'''
'''思路：就是间隔遍历一棵树
		分两种情况：1.遍历这个跟节点，那么他的两个孩子就不能遍历，故只能遍历
					root + root.left.left + root.left.right
					2.不遍历这个根节点，那么必须遍历他的两个孩子,即
					root.left + root.right'''
class Solution(object):
	def rob(self, root: TreeNode) -> int:
		# 大量重复
		if not root:
			return  0
		res1 = root.val
		if root.left:
			res1 += self.rob(root.left.left) + self.rob(root.left.right)
		if root.right:
			res1 += self.rob(root.right.left) + self.rob(root.right.right)
		res2 = self.rob(root.left) + self.rob(root.right)
		return max(res1, res2)


	def rob(self, root: TreeNode) -> int:
		''' 由于左右孩子分别是自己两颗子树的根节点，所以上述两种情况实际都是一种情况，
		 就是这个根节点到底取不取，所以对于每个节点都有两种情况：取；不取
		用一个长度为2的列表来存储每个节点的情况'''	
		def helper(root):
			if not root:
				return [0, 0]
			left = helper(root.left)
			right = helper(root.right)
			rob = root.val + left[1] + right[1] # 第二元素为不取的值
			skip = max(left) + max(right) # 因为根节点不抢，所有左右子随意抢
			return [rob, skip]
		
		res = helper(root)
		return max(res)
