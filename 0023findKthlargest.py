'''215问题描述：在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。'''
'''知识点：
	快排： 需要先打乱数组
	堆：
		用于求解 TopK Elements 问题，也就是 K 个最小元素的问题。可以维护一个大小为 K 的最小堆，最小堆中的元素就是最小元素。最小堆需要使用大顶堆来实现，大顶堆表示堆顶元素是堆中最大元素。这是因为我们要得到 k 个最小的元素，因此当遍历到一个新的元素时，需要知道这个新元素是否比堆中最大的元素更小，更小的话就把堆中最大元素去除，并将新元素添加到堆中。所以我们需要很容易得到最大元素并移除最大元素，大顶堆就能很好满足这个要求。
KTop 大：小堆顶  此题用小堆顶
KTOP 小：大堆顶

堆也可以用于求解 Kth Element 问题，得到了大小为 k 的最小堆之后，因为使用了大顶堆来实现，因此堆顶元素就是第 k 小的元素。

快速选择也可以求解 TopK Elements 问题，因为找到 Kth Element 之后，再遍历一次数组，所有小于等于 Kth Element 的元素都是 TopK Elements。

可以看到，快速选择和堆排序都可以求解 Kth Element 和 TopK Elements 问题。'''
'''python中使用heapq模块，可以使用堆，其默认是小堆顶
FUNCTIONS
    heapify(...)
        Transform list into a heap, in-place, in O(len(heap)) time.
    
    heappop(...)
        Pop the smallest item off the heap, maintaining the heap invariant.
    
    heappush(...)
        heappush(heap, item) -> None. Push item onto heap, maintaining the heap invariant.
    
    heappushpop(...)
        heappushpop(heap, item) -> value. Push item on the heap, then pop and return the smallest item
        from the heap. The combined action runs more efficiently than
        heappush() followed by a separate call to heappop().
    
    heapreplace(...)
        heapreplace(heap, item) -> value. Pop and return the current smallest value, and add the new item.
        
        This is more efficient than heappop() followed by heappush(), and can be
        more appropriate when using a fixed-size heap.  Note that the value
        returned may be larger than item!  That constrains reasonable uses of
        this routine unless written as part of a conditional replacement:
        
            if item > heap[0]:
                item = heapreplace(heap, item)
    
    merge(*iterables)
        Merge multiple sorted inputs into a single sorted output.
        
        Similar to sorted(itertools.chain(*iterables)) but returns a generator,
        does not pull the data into memory all at once, and assumes that each of
        the input streams is already sorted (smallest to largest).
        
        >>> list(merge([1,3,5,7], [0,2,4,8], [5,10,15,20], [], [25]))
        [0, 1, 2, 3, 4, 5, 5, 7, 8, 10, 15, 20, 25]
    
    nlargest(n, iterable, key=None)
        Find the n largest elements in a dataset.
        
        Equivalent to:  sorted(iterable, key=key, reverse=True)[:n]
    
    nsmallest(n, iterable, key=None)
        Find the n smallest elements in a dataset.
        
        Equivalent to:  sorted(iterable, key=key)[:n]'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
		'''最为暴力，但是时间复杂度为O(NlogN)'''
		return nums.sort()[-k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
		'''利用小堆顶，时间复杂度为O(NlogK)'''
        import heapq
        a = nums[:k]
        heapq.heapify(a)
        for i in range(k, len(nums)):
            heapq.heappushpop(a, nums[i])
        return a[0]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        '''快速排序求解,利用中轴元素的位置求解'''
        k = len(nums) - k
        l, r = 0, len(nums)-1
        while True:
            flag = self.quicksort(nums, l, r)
            if flag == k:
                break
            elif flag > k:
                r = flag - 1
            else:
                l = flag + 1
        return nums[k]
    
    def quicksort(self, nums, l, r):
		'''双指针，现将首元素复制'''
        n = nums[l]
        while l < r:
            while l < r and nums[r] >= n:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= n:
                l += 1
            nums[r] = nums[l]
        nums[l] = n
        return l	
