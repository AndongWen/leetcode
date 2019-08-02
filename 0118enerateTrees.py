'''95不同的二叉搜索树:
	给定一个整数 n，生成所有由 1 ... n 为节点所组成的二叉搜索树。'''
'''思路：分治，利用二叉搜索树的特点。'''
class TreeNode():
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution():
	def generateTrees(self, n):
		if n < 1:
			return []
		return self.generateN(1, n)

	def generateN(self, start, end):
		trees = []
		if start > end:
			return [None]
		elif start == end:
			return [TreeNode(end)]
		else:
			for i in range(start, end+1):
				left = self.generateN(start, i-1)
				right = self.generateN(i+1, end)
				for l in left:
					for r in right:
						root = TreeNode(i)
						root.l = l
						root.r = r
						trees.append(root)
		return trees	

	def generateTrees(self, n):
		'''使用动态规划，就是记录长度为n的所有可能结果
			长度为0：根节点为空
			长度为1：根节点，左右节点都为空就一种情况；
			长度为2：根节点，左右节点有一个为空，两种情况
			长度为3可以转化为上述三种情况的组合'''
		if n == 0:
			return []
		dp = [[] for _ in range(n+1)] # 初始化
		dp[0].append(None)
		for i in range(1, n+1): # 从dp[1]开始对dp进行赋值
			for j in range(1, i+1): # 考虑左右子树长度的所有可能
				leftLen = j-1 # 左子树的长度
				rightLen = i-j # 右子树的长度
				for l in dp[leftLen]:
					for r in dp[rightLen]:
						root = TreeNode(j)
						root.left = l # 起初左边一定小于右边,所以后续左子树是在共享子树
						root.right = self.clone(r, j)
						dp[i].append(root)

		return dp[n]
	
	def clone(self, root, n):
		'''对同种结构的树进行复制，修改对应的val'''
		if root == None:
			return None
		node = TreeNode(root.val+n)
		node.left = self.clone(root.left, n)
		node.right = self.clone(root.right, n)
		return node

def main():
	s = Solution()
	a = s.generateTrees(3)
	for i in a:
		print(a)

if __name__ == "__main__":
	main()

