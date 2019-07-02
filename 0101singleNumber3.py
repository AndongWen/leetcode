'''260给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。'''
'''利用 x ^ 1s = ~x 的特点，可以将位级表示翻转；利用 x ^ x = 0 的特点，可以将三个数中重复的两个数去除，只留下另一个数。
利用 x & 0s = 0 和 x & 1s = x 的特点，可以实现掩码操作。一个数 num 与 mask：00111100 进行位与操作，只保留 num 中与 mask 的 1 部分相对应的位。
利用 x | 0s = x 和 x | 1s = 1s 的特点，可以实现设值操作。一个数 num 与 mask：00111100 进行位或操作，将 num 中与 mask 的 1 部分相对应的位都设置为 1。
位与运算技巧：

n&(n-1) 去除 n 的位级表示中最低的那一位。例如对于二进制表示 10110100，减去 1 得到 10110011，这两个数相与得到 10110000。
n&(-n) 得到 n 的位级表示中最低的那一位。-n 得到 n 的反码加 1，对于二进制表示 10110100，-n 得到 01001100，相与得到 00000100。
n-n&(~n+1) 去除 n 的位级表示中最高的那一位'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ret = 0
        for i in range(len(nums)):
            ret ^= nums[i]
         
        ret &= -ret # 获取最右边一位得1，以此将这两个不重复得数区分开来开
        
        res = [0]*2
        for i in range(len(nums)):
            if nums[i] & ret == 0:
                res[0] ^= nums[i]
            else:
                res[1] ^= nums[i]
              
        return res