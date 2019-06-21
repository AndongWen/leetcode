'''108将有序数组转化为二叉搜索树:
将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。'''

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
		'''利用BST的特性'''
        if not nums:
            return None
        n = len(nums)
        target = n//2
        root = TreeNode(nums[target])
        root.left = self.sortedArrayToBST(nums[: target])
        root.right = self.sortedArrayToBST(nums[target+1:]) 
        return root

