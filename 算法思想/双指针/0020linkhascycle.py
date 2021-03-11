'''问题描述：给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。'''
class Solution(object):
	'''解法1：哈希表 将遍历过得节点的引用存在哈希表中，若遍历的下一个节点的
			  引用在哈希表中，则有环；若是遍历的下一个节点是None，则无环
	   解法2：双指针，快慢指针，如有环，两个指针必相遇'''
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
