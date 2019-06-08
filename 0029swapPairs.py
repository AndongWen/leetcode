'''24两两交换链表中的节点：
   给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
		'''递归'''
        while head is None or head.next is None:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next

    def swapPairs(self, head: ListNode) -> ListNode:
		'''迭代'''
        p = ListNode(0)
        p.next = head
        temp = p
        while temp.next is not None and temp.next.next is not None:
			'''画图很好理解：需要三个指针进行维护，两个为正在进行交换的
			   节点，剩下的那个用来表示已经交换好的链表尾部'''
            start = temp.next
            end = temp.next.next
            temp.next = end
            start.next = end.next
            end.next = start
            temp = start
        return p.next
