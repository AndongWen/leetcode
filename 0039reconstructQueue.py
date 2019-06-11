'''406根据身高重新建立队列
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。'''
'''思路：先插入身高小的元素，那么后插入身高大的元素若在小元素前面，
	必定会改变身高小的K值,进而导致失败
	那么先插入大身高的元素，后插入的小身高的元素也不会影响大身高元素的k
	由于大身高的元素先插入，所以后插入的元素的位置就可以由他对应的k确定
	
	所以先排序: 按照身高降序，K值升序'''
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key = lambda x: (-x[0], x[1]))
        for per in people:
            res.insert(per[1], per)
        return res
