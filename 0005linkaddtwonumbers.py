# 定义链表的节点
class LinkNode(object):
	def __init__(self,x):
		self.val = x
		self.next = None


class Solution(object):
	def addtwonumber1(self, l1, l2):
		'''转换为字符串'''
		str1, str2 = '', ''
		p, q = l1, l2
		while p is not None:
			str1 = str(p.val) + str1
			p = p.next
		while q is not None:
			str2 = str(q.val) + str2
			q = q.next
		sum  = str(int(str1)+int(str2))
		l3 = l4 = LinkNode(0)
		for i in range(len(sum), 0, -1):
			l3.next = LinkNode(int(sum[i-1]))
			l3 = l3.next
		return l4.next
		
	def addtwonumber2(self, l1, l2):
		'''直接加'''
        l3 = l4 = ListNode(0)
        carry = 0
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = (a+b+carry)%10
            carry = (a+b+carry)//10
            l3.next = ListNode(sum)
            l3 = l3.next
            if l1 != None: l1 = l1.next # None没有next属性
            if l2 != None: l2 = l2.next
        if carry > 0:
            l3.next = ListNode(1)
        return l4.next
