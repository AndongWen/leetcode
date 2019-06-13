'''452最少的标引爆气球:在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以y坐标并不重要，因此只要知道开始和结束的x坐标就足够了。开始坐标总是小于结束坐标。平面内最多存在104个气球。

一支弓箭可以沿着x轴从不同点完全垂直地射出。在坐标x处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足  xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。'''
'''类似于不重叠区间的个数:都是更加看中区间的尾部'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
		'''按照区间的头部排序,但实际是尾部决定'''
        points.sort()
        count = 1
        if not points:
            return 0
        end  = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] <= end:
                end = min(end, points[i][1]) # 下一区间的头部必须小于前面最小的end，否则就要加一支箭
            else:
                end = points[i][1]
                count += 1
        return count

    def findMinArrowShots2(self, points: List[List[int]]) -> int:
		'''按照尾部排序'''
        points.sort(key=lambda x: x[1])
        res, end = 0, float('-inf')
        for p in points:
            if p[0] > end:
                res += 1
                end = p[1]
        return res
