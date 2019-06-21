'''109有序链表转换为二叉搜索树
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
#        nums = []
#        while head:
#            nums.append(head.val)
#            head = head.next
#        
#        def helper(nums):
#            if not nums:
#                return None
#            target = len(nums)//2
#            root = TreeNode(nums[target])
#            root.left = helper(nums[:target])
#            root.right = helper(nums[target+1:])
#            return root
#        
#        root = helper(nums)
#        return root
        
#        快慢指针找中间链表
#        def helper(head, tail):
#            if head == tail:
#                return # 此处不要返回值 画图可以理解
#            slow, fast = head, head
#            while fast.next != tail and fast.next.next != tail:
#                slow = slow.next
#                fast = fast.next.next
#            root = TreeNode(slow.val)
#            root.left = helper(head, slow)
#            root.right = helper(slow.next, tail)
#            return root
#        
#        return helper(head, None)

#       利用树得中序遍历
        self.head = head
        n = 0
        while head:
            n += 1 # 计数
            head = head.next 
            
        def helper(l, r):
            if l > r:
                return
            m = l + (r-l)//2
            left = helper(l, m-1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = helper(m+1, r)
            return root
        
        return helper(1, n)
