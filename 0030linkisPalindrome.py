'''234请判断一个链表是否为回文链表。'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        '''仅仅考虑遍历，不利用任何辅助工具''' 
        '''解法：快慢指针，快指针速度为慢指针得两倍 O(n)
                将链表分为两部分，将一部链表反转 O(n)
                之后一一比对O(n)'''
        if head is None or head.next is None:
            return True
        slow = head
        fast = head.next
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        if fast is not None: # 偶数节点，让slow指向下一节点
            slow = slow.next
        self.cut(head, slow)
        return self.is_equal(head, self.reverse(slow))
    
    def cut(self, head: ListNode, cutnode: ListNode) -> None:
        while head.next != cutnode:
            head = head.next
        head.next = None
        
    def is_equal(self, l1: ListNode, l2: ListNode) -> bool:
        while l1: # 原链表有偶数节点的时候，l1与l2的长度一致
				  # 奇数节点时，l1比l2短1
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next
        return True
    
    def reverse(self, head: ListNode) -> ListNode: # 206链表反转
        cur = head
        pre = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def isPalindrome2(self, head: ListNode) -> bool:
		'''空间复杂度不'''
        if head == None or head.next == None:
            return True
        target = []
        while head:
            target.append(head.val)
            head=head.next
        p = (len(target)-1)//2+1
        q = (len(target))//2
        
        return target[0:p]==target[q:len(target)][::-1]
