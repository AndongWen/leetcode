'''128最长连续序列：
	给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。'''

class Solution():
	def longestConsecutive(self, nums):
		hash_dict = dict()
        
		max_length = 0
		for num in nums:
			if num not in hash_dict:
				left = hash_dict.get(num - 1, 0)　# 没有则获取对应的默认值，不设置这个值
				right = hash_dict.get(num + 1, 0)

				cur_length = 1 + left + right
				if cur_length > max_length:
					max_length = cur_length

				hash_dict[num] = cur_length
				hash_dict[num - left] = cur_length
				hash_dict[num + right] = cur_length

		return max_length	

	def longestConsecutive(self, nums):

        hashset = set(nums)
        longest = 0
        for num in hashset:
            if num-1 not in hashset: #　从num-1开始，因为num一定出现在某个序列里面了
                curnum = num
                curlength = 1
            
                while curnum + 1 in hashset:
                    curnum += 1
                    curlength += 1
                
                longest = max(longest, curlength)
          
        return longest
def main():
	a = Solution()
	nums = [100,4,200,1,3,2]
	b = a.longestConsecutive(nums)
	print(b)

if __name__ == '__main__':
	main()
		
