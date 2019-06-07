'''21将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。'''
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		'''递归
			我们可以如下递归地定义在两个链表里的 merge 操作（忽略边界情况，比如空链表等）：

{ 
list1[0]+merge(list1[1:],list2)
list2[0]+merge(list1,list2[1:])
  
 

也就是说，两个链表头部较小的一个与剩下元素的 merge 操作结果合并'''
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
		# 迭代 
        head = ListNode(0) # 仅仅用来标记返回得链表
        pre = head # 用来形成最后链表得指针
        while l1 and l2:
            if l1.val <= l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        # l1和l2肯定有一个为空
        pre.next = l1 if l1 else l2 # 也可以处理特殊情况:一开始l1和l2同时为空
        return head.next
