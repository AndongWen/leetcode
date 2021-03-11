'''问题描述:给定一个二叉树，返回其按层次遍历的节点值。
 （即逐层地，从左到右访问所有节点）。
	每层为一个列表'''
class Solution(object):
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
		'''递归解法'''
        levels = []
        if not root:
            return levels
        
        def helper(node, level): 
			'''level为当前访问的层数，当前最高层数就是levels的长度，
		如果两者相等，就向levels 中添加一个空列表 列表的下标从0开始'''
            if len(levels) == level:
                levels.append([])
                
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
                
        helper(root, 0)
        return levels

	def levelOrder2(self, root:TreeNode) -> list[list(int)]:
		'''非递归:核心点在于如何将每一层封装到一个列表中
			计算当前层有多少个元素：其等于队列的长度
			将队列中元素依次弹出，加入当前层的列表中
			在进入到下一层的列表中'''
		res = []
		if not root:
			return res
		queue = [root]
		while queue:
			ans = []
			len_queue = len(queue)
			for i in range(len_queue):
				node = queue.pop(0)
				ans.append(node.val)
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			res.append(ans)
		return res
			
