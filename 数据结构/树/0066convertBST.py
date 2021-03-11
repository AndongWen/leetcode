'''538把二叉搜索树转换为累加树
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。'''
'''思路:中序遍历，先遍历右子树'''
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        sum = 0
        q = coll.deque()
        cur = root
        
        while cur or q:
            while cur:
                q.append(cur)
                cur = cur.right
                
            cur = q.pop()
            cur.val += sum
            sum = cur.val
            cur = cur.left
         
        return root

    def convertBST2(self, root: TreeNode) -> TreeNode:
		'''递归'''
        self.sum = 0       
        self.travell(root)
        return root
    
    def travell(self, root: TreeNode):
        if not root:
            return 
        self.travell(root.right)
        root.val += self.sum
        self.sum = root.val
        self.travell(root.left)
