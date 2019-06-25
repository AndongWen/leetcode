'''283移动０：给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。(就地操作，尽可能减少操作次数)'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#        笨方法
#        cnt = 0
#        for i in range(len(nums)):
#            if nums[i] == 0:
#                cnt += 1
#        for i in range(cnt):
#            nums.remove(0)
#        for i in range(cnt):
#            nums.append(0)
            
#        先将不为0得数字移动到前面，然后补充0
#        index = 0
#        for i in range(len(nums)):
#            if nums[i] != 0:
#                如果nums[i]前面没有0，此步就是多余得，可以改进
#                nums[index] = nums[i]
#                index += 1
#        while index < len(nums):
#            nums[index] = 0
#            index += 1

        index = 0 # 用于寻找第一个为0得值得索引
        for i in range(len(nums)):
            if nums[i] != 0:
                if nums[index] == 0:
                    nums[index], nums[i] = nums[i], nums[index]
                index += 1
