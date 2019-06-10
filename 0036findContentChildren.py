'''455假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。对每个孩子 i ，都有一个胃口值 gi ，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j ，都有一个尺寸 sj 。如果 sj >= gi ，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。

注意：

你可以假设胃口值为正。
一个小朋友最多只能拥有一块饼干'''
'''解法1：若最小的饼干不能分配给这个胃口最小的朋友，就放弃这个饼干'''
'''解法2：若最大的饼干不能分配给这个胃口最大的朋友，就放弃这个饼干'''
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
		'''直接排序'''
        i, j = 0, 0
        count = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                count += 1
                i += 1
            j += 1
        return count

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
		'''利用堆'''
        import heapq
        count = 0
        heapq.heapify(g)
        heapq.heapify(s)
        while g and s:
            if g[0] <= s[0]:
                count += 1
                heapq.heappop(g)
            heapq.heappop(s)
        return count
     
