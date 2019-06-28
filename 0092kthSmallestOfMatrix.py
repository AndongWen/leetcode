'''378有序矩阵中第k小的元素：
	给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
请注意，它是排序后的第k小元素，而不是第k个元素。'''
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#		 利用堆　heapq是小堆顶
#        n = len(matrix)
#        a = []
#        for i in range(k):
#            a.append(-matrix[i//n][i%n])
#        heapq.heapify(a)
#        for i in range(k, n*n):
#            heapq.heappushpop(a, -matrix[i//n][i%n])
#        return -a[0]
         # 二分法
        low = matrix[0][0]
        high = matrix[-1][-1]
        while low < high:
            mid = low + (high-low)//2
            cnt = self.kthsearch(matrix, mid)
            if cnt < k:
                low = mid +1
            else:
                high = mid
        return high
              
    def kthsearch(self, matrix, target):
        n = len(matrix)
        i = n -1
        j = 0
        res = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= target:
                res += i+1
                j += 1
            else:
                i -= 1
        return res 
