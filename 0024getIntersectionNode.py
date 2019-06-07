'''160:编写一个程序，找到两个单链表相交的起始节点。'''
class Solution(object):
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
		思路：要求时间复杂度为 O(N)，空间复杂度为 O(1)。如果不存在交点则返回 null。

设 A 的长度为 a + c，B 的长度为 b + c，其中 c 为尾部公共部分长度，可知 a + c + b = b + c + a。

当访问 A 链表的指针访问到链表尾部时，令它从链表 B 的头部开始访问链表 B；同样地，当访问 B 链表的指针访问到链表尾部时，令它从链表 A 的头部开始访问链表 A。这样就能控制访问 A 和 B 两个链表的指针能同时访问到交点。

如果不存在交点，那么 a + b = b + a，以下实现代码中 l1 和 l2 会同时为 null，从而退出循环。
        """
        l1 = headA
        l2 = headB
        while l1 != l2:
            l1 = headB if l1 == None else l1.next
            l2 = headA if l2 == None else l2.next
        return l1

	def getIntersectionNode2(self, headA, headB):
    	'''思路：由于两个链表后面部分一样(如果有公共部分),两个链表长度的差是由前面产生的。所以先求两个链表的长度，然后在让相对长的链表走到跟短链表相同长度的位置，然后再一起遍历，找到相等的位置，返回。若没有找到，返回None。时间复杂度O(n), 空间复杂度O(l)'''		
		        def countlen(head):
            count = 0
            while head is not None:
                count += 1
                head = head.next
            return count
        
        if not headA or not headB:
            return None
        lenA = countlen(headA)
        lenB = countlen(headB)
        if lenA < lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        for i in range(lenA-lenB):
            headA = headA.next
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

'''另一种解法：将两个链表分别保存到两个列表中，倒着来取其中的值'''
