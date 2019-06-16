'''111给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。'''

class Solution:
    def minDepth(self, root: TreeNode) -> int:
		'''递归'''
        if not root:
            return 0
        l_depth = self.minDepth(root.left) + 1
        r_depth = self.minDepth(root.right) + 1
        if l_depth == 1 or r_depth == 1: # 此处需要注意，当左右子树有一个为空时
										 # 需要返回另一侧子树的深度，若返回min，
										 # 则表明此节点为叶节点
            return l_depth+r_depth-1
        return min(l_depth, r_depth)

    def minDepth(self, root: TreeNode) -> int:
		'''迭代：使用栈：Dfs
		   必须访问完每个节点'''
		        if not root:
            return 0
        q = coll.deque()
        q.append((root, 1))
        min_depth = float('inf')
        while q:
            node, curdepth = q.pop()
            if not node.right and not node.left:
                min_depth = min(curdepth, min_depth)
            if node.left:
                q.append((node.left, curdepth+1))
            if node.right:
                q.append((node.right, curdepth+1))
        return min_depth  

    def minDepth(self, root: TreeNode) -> int:
		'''迭代：使用栈：bfs
		   第一次碰到的叶子节点就是最短路径对应的叶子节点'''
		if not root:
            return 0
        q = coll.deque()
        q.append((root, 1))
        while q:
            node, curdepth = q.popleft()
            if not node.right and not node.left:
				return curdepth
            if node.left:
                q.append((node.left, curdepth+1))
            if node.right:
                q.append((node.right, curdepth+1))
