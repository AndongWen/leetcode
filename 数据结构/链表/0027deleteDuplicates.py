'''83给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。'''
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
		'''直接法'''
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
		'''递归'''
		if head is None or head.next is None:
			return head
		head.next = self.deleteDuplicates2(head.next)
		return head.next if head.val == head.next.val else head	
