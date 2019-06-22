'''501二叉搜索树的众树：给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。'''

'''思路：依旧是利用中序遍历有序，，先设置一个空列表res，每次遍历一个节点，
		将其与前面的进行比较，若相等则将curtimes+1，反之将curtimes设置为1；
		之后与maxtimes进行比较，相等则将对应的root.val加入到res中；比maxtimes大
		则重置res，将root.val加入'''

class Solution(object):
	# 此解法　空间复杂度为常数
	# 还可以遍历整个树，将节点数据存在一个列表中，使用collections.Counter计数
	# 然后找到出现最多的次数，之后将对应的键添加到列表中
	def __init__(self):
		self.res = []
		self.pre = None
		self.maxtimes = 0
		self.curtimes = 1 # 从第二的节点开始判断,第一个节点默认出现一次

	def findnode(self, root)
		self.inordertravell(root)
		return self.res

	def inordertravell(self, root):
		if not root:
			return
		self.inordertravell(root.left)
		if self.pre:
			if self.pre.val == root.val:
				self.curtimes += 1
			else:
				self.curtimes = 1 # 此时root与pre不等，已经出现一次
		if self.curtimes == self.maxtimes:
			res.append(root.val)
		elif self.curtimes > self.maxtimes:
			self.maxtimes = self.curtimes
			res = [root.val]
		self.pre = root 
		self.inordertravell(root.right)
	
