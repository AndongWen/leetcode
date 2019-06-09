'''给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。'''
ass Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
		'''使用三指针，有点类似快排中的第二种，里面的特殊情况'''
        p = 0 # 标记0区域得右边界
        q = len(nums)-1 # 标记2区域得左边界
        cur = 0 # 正在处理得元素
        while cur <= q:
            if nums[cur] == 0:
                nums[cur], nums[p] = nums[p], nums[cur]
                cur += 1
                p += 1
            elif nums[cur] == 2:
                nums[cur], nums[q] = nums[q], nums[cur]
                q -= 1
            else:
                cur += 1

'''
0元素取出来扔到最后面，2元素取出来扔到最前面，1元素不处理
从头开始遍历
    1. 元素nums[i]为0 从当前位置弹出，插入到nums最前面 i自加 
    2. 元素nums[i]为1 不做处理，i自加跳过
    3. 元素nums[i]为2 从当前位置弹出，插入到nums最后面 N自减 i不要自加

'''

class Solution(object):
    def sortColors(self, nums):
        N = len(nums)
        i = 0
        while i < N:
            if nums[i] == 2:
                nums.pop(i)
                nums.append(2)
                N -= 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 0:
                nums.pop(i)
                nums.insert(0,0)
                i += 1
