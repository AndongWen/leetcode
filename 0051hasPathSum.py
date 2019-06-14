'''112路径总和：给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。'''
'''思路：显然要遍历到树的叶子节点处，可以考虑递归，每次到一个节点，可以将
		sum -= root.val, 到达叶子节点看sum == 0?
		每次到一个节点需要有两个分支，一左一右'''

'''递归：正好对应BFS，广度优先搜索
   迭代：为DFS，深度优先搜索
	深度优先搜索在除了最坏情况下都比广度优先搜索更快。最坏情况是指满足目标和的 root->leaf 路径是最后被考虑的，这种情况下深度优先搜索和广度优先搜索代价是相通的。'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		'''时间复杂度：我们访问每个节点一次，时间复杂度为 O(N)，其中N是节点个数。
空间复杂度：最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，递归会调用 N次（树的高度），因此栈的空间开销是O(N) 。但在最好情况下，树是完全平衡的，高度只有log(N)，因此在这种情况下空间复杂度只有O(log(N)) 。'''
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
		'''时间复杂度：和递归方法相同是O(N)。
空间复杂度：当树不平衡的最坏情况下是O(N)。在最好情况（树是平衡的）下是O(logN)。'''
        if not root:
            return False
        res = [(root, sum-root.val)]
        while res:
            curnode = res.pop()
            if curnode[1] == 0 and not curnode[0].left and not curnode[0].right:
                return True
            if curnode[0].right:
                res.append((curnode[0].right, curnode[1]-curnode[0].right.val))
            if curnode[0].left:
                res.append((curnode[0].left, curnode[1]-curnode[0].left.val))
        return False 
