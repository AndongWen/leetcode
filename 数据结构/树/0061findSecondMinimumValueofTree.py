'''给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么这个节点的值不大于它的子节点的值。 

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。'''
class Solution(object):
	def findSecondMinimumValue(self, root):
		'''思路：遍历整个树，找到比根节点大的最小的节点'''
		self.min = float('inf')
		self.flag = 0 # 标记量，标记是否有比根节点大的点出现

		def eachnode(root, k): # k为跟节点的值
			# 通过遍历找到，比根节点大的最小节点数值
			if root:
				if root.val < self.min and root.val > k:
					self.flag = 1
					self.min = root.val
				eachnode(root.left, k)
				eachnode(root.right, k)
	
		if root:
			eachnode(root, root.val)
			if self.flag:
				return self.min
		return -1

	def findSecondMinimumValue2(self, root):
		'''思路：递归：
				一个节点若有孩子，则节点的值一定最小，所以只要返回孩子的最小值即可，但要注意
				孩子的值可能与父节点一样大'''
		if not root:
			return -1
		if not root.left and not root.right:
			return -1
		leftval = root.left.val
		rightval = root.right.val
		if leftval == root.val:
			leftval = self.findSecondMinimumValue2(root.left)
		if rightval == root.val:
			rightval = self.findSecondMinimumValue2(root.right)
		if rightval != -1 and leftval != -1:
			return min(rightval, leftval)
		if rightval == -1 and leftval == -1:
			return -1
		if leftval == -1:
			return rightval
		return leftval
		
