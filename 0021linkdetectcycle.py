'''问题描述：给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环.'''
'''验证是否有环，解法同0020，但是双指针那块：
有一个纯数学的快慢指针解法，设环的起始节点为 E，快慢指针从 head 出发，快指针速度为 2，设相交节点为 X，head 到 E 的距离为 H，E 到 X 的距离为 D，环的长度为 L，那么有：快指针走过的距离等于慢指针走过的距离加快指针多走的距离（多走了 n 圈的 L） 2(H + D) = H + D + nL，因此可以推出 H = nL - D，这意味着如果我们让俩个慢指针一个从 head 出发，一个从 X 出发的话，他们一定会在节点 E 相遇

				  _____
				 /     \
		 head___________E       \
				\       /
				 X_____/ 
'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # flag = False
        # if head is None:
        #    return None
        slow = head
        fast = head
        while fast and fast.next: # 循环的条件是有环 利用判断的短路特性
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # flag = True
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
