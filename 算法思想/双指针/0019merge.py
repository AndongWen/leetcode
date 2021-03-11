'''问题描述：给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。

说明:

初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        '''从后往前归并'''
        index1 = m-1
        index2 = n-1
        mergeindex = m+n-1
        while index1 >= 0 and index2 >= 0: # 两者都不为空时，进行比较
            if nums1[index1] >= nums2[index2]:
                nums1[mergeindex] = nums1[index1]
                index1 -= 1
            else:
                nums1[mergeindex] = nums2[index2]
                index2 -=1
            mergeindex -= 1
            
        # 总有一个会先比较结束，若是nums1剩余，则不需要移动，此时index2为0
		# 若是nums2剩余，直接全部移动过来
        nums1[:index2+1] = nums2[:index2+1]
