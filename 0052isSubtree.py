'''572子树：给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。
'''
'''思路1：与路径总和3一样,s中的每一个节点都可能是t中的根节点
		递归：什么时候返回false? s与t中一个为空一个非空，两者都不为空时值不等
			  什么时候返回True？上者的对立面，两者都不为空且值相同？此时还要继续向下
								走，直到s与t都为空
			  由于s中所有节点都可能是t中的根节点，所以需要重新写个函数
   思路2:依次先序遍历两颗树，使用列表保存节点里面的值，为空时输入一个特殊字符，之后
		 将两个列表转换为字符串，判断后者是不是前者的子串即可'''

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return False
        return self.isSubtreeRoot(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSubtreeRoot(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.isSubtreeRoot(s.left, t.left) and self.isSubtreeRoot(s.right, t.right)

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        res1 = []
        res2 = []
        
        def explore(node: TreeNode, res: list):
            if node:
                res.append(',' + str(node.val)) # 需要加，分隔开，不然当数值出现两位
												# 以上时会出现错误
                explore(node.left, res)
                explore(node.right, res)
            else:
                res.append(',' + "#")
                
        explore(s, res1)
        explore(t, res2)
        return ''.join(res2) in ''.join(res1)
