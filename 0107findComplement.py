'''476.数字的补数：给定一个正整数，输出它的补数。补数是对该数的二进制表示取反。'''
'''思路：不可以直接去反，因为默认是32位全部取反,实际就是找到与num有效位数一致的111掩码
	再mask^num'''
class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        mask = 1 << 31
        while num & mask == 0:
            mask >>= 1 # 找到与num位数一致的地方
        mask = (mask<<1) -1
        return mask^num
