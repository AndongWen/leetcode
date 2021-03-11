'''19给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。n数字有效'''
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		'''一般性情况：快慢指针，一个先跑n，之后两个同时跑，当块指针到达最后一个节点时
		   慢指针正好到倒数第n+1个，则slow.next = slow.next.next'''
        slow = fast = head
        for i in range(n):
            fast = fast.next
        if fast is None: # 说明到达最尾，即删除得是第一个节点
            return head.next
        while fast.next is not None: # 到达最后一个节点
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
