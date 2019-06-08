'''725给定一个头结点为 root 的链表, 编写一个函数以将链表分隔为 k 个连续的部分。

每部分的长度应该尽可能的相等: 任意两部分的长度差距不能超过 1，也就是说可能有些部分为 null。

这k个部分应该按照在链表中出现的顺序进行输出，并且排在前面的部分的长度应该大于或等于后面的长度。

返回一个符合上述规则的链表的列表'''
'''思路：
		数组中所有的链表长度中，最大只能比最小的大一
		如果数组中有[]，则非空的链表一定长度一致
        size = num // k # 表明一组里面最少有几个节点
        mod = num % k # 表明有几组要拥有a+1个节点
'''
		
class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
		
        res = [None] * k
        num = 0
        head = root
        while head:
            num += 1
            head = head.next
        size = num // k # 表明一组里面最少有几个节点
        mod = num % k # 表明有几组要拥有a+1个节点
        cur = root
        for i in range(k):
            if cur == None:
                break
            res[i] = cur
            a = size
            if mod > 0:
                a += 1
                mod -= 1
            for i in range(a-1):
                cur = cur.next 
            temp = cur.next
            cur.next = None
            cur = temp
        return res

class Solution:
    def splitListToParts(self, root, k):
        # Count the length of the linked list
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        # Determine the length of each chunk
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
        # Split up the list
        prev, curr = None, root
        for index, num in enumerate(res):
            if prev:
                prev.next = None
            res[index] = curr
            for i in range(num):
                prev, curr = curr, curr.next
        return res
