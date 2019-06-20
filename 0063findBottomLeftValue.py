'''513找树左下角的值：给定一个二叉树，在树的最后一行找到最左边的值。'''
import collections as coll

class Solution(object):
	def findBottomLeftValue(self, root: TreeNode) -> int:
		'''层次遍历，取最后一个元素的第一个值 '''		
		levels = []
		if not root:
			return levels
		
		def helper(root, level):
			if len(levels) == level:
				levels.append([])
			
			levels[level].append(root.val)
			if root.left:
				helper(root.left, level+1)
			if root.right:
				hepler(root.right, level+1)	

		helper(root, 0)
		return levels[-1][0]

    def findBottomLeftValue(self, root: TreeNode) -> int:
		'''改变层次遍历的顺序:从右到左'''
        q = coll.deque()
        if not root:
            return None
        q.append(root)
        
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
               
        return node.val


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        a=[root]
        while True:
            b=[]
            for n in a:
                for n in (n.left,n.right):
                    if n:
                        b.append(n)
            if not b:
                return a[0].val
            a=b
