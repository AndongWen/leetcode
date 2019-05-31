'''问题描述：
	数组arr是[0, 1, ..., arr.length - 1]的一种排列，
	我们将这个数组分割成几个“块”，并将这些块分别进行排序。
	之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

	我们最多能将数组分成多少块？'''
class Solution(object):
	def maxChunksToSorted(self, arr):
		'''思路：此数组有特殊性，经过排列后，元素大小与元素的下标一致
		   切分点的特点：左侧最大值小于右侧最小值
		   由于数组arr的特殊性，arr[:i+1]的最大值left_max只存在两种情况：

        left_max==i，则右边的最小值一定大于i，可以作为一个切分点
        left_max>i，则右边一定存在小于i的数，则不可以作为切分点'''
		flag, count = 0, 0
		for i in range(len(arr)):
			if flag < arr[i]:
				flag = arr[i]
			if flag == i:
				flag += 1
				count += 1
		return count
