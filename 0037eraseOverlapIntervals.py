'''435无重叠区间：给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
		'''贪心算法：
		   先计算最多能组成的不重叠区间个数，然后用区间总个数减去不重叠区间的个数。

在每次选择中，区间的结尾最为重要，选择的区间结尾越小，留给后面的区间的空间越大，那么后面能够选择的区间个数也就越大。

按区间的结尾进行排序，每次选择结尾最小，并且和前一个区间不重叠的区间。'''
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not len(intervals):
        	return 0
        intervals = sorted(intervals, key=lambda k:k.end)
        minEnd = intervals[0].end
        rest = 1
        for i in range(1,len(intervals)):
        	if intervals[i].start < minEnd:
        		continue
        	rest += 1
        	minEnd = intervals[i].end

        return len(intervals) - rest
