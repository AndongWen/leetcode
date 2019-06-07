'''206反转一个链表'''
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''low解法'''        
        if head is None:
            return None
        p = []
        while head:
            p.append(head)
            head = head.next
        lenp = len(p)
        head = p[-1]
        for i in range(len(p)-1, 0, -1):
            q = p[i]
            q.next = p[i-1]
        p[0].next = None
        return head

    def reverseList2(self, head: ListNode) -> ListNode:
        '''迭代:遍历一次链表，将每次遍历到的节点，指针域指向上一个节点
			则需要保存上一个节点,同时也要保存下一个节点，否则会丢失'''        
        prev = None
        cur = head
        while cur is not None:
            next = cur.next # 暂时保存下一个节点
            cur.next = prev
            prev = cur
            cur  = next
        return prev
       
    def reverseList3(self, head: ListNode) -> ListNode:
        '''递归'''        
        if head is None or head.next is None: 
			'''head :防止链表为空
			   head.next is None:head为链表中最后一个节点'''
            return head
        p = self.reverseList3(head.next) # 仅用来保存最后一个节点的引用，即返回指针的head
        head.next.next = head
        head.next = None
        return p 
