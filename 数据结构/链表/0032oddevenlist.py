'''给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。'''
'''思路：遍历过程中，将奇数节点链接起来，偶数节点链接起来，但记得保存第一个偶节点'''
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd = head
        even = evenhead = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next
		# 只要将最后一个奇数节点的next指向第一个偶数节点即可
        # 若节数为偶数，偶数节点的最后本来就指向None
        # 若节点数为奇数，最后一个节点指向None，在循环中最后一个even会成为这个None
        odd.next = evenhead
        return head
