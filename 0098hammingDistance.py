'''461:两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
		'''异或然后统计１的位数'''
        z = x^y
        cnt = 0
        while z!=0:
            if (z&1 == 1):
                cnt += 1
            z = z >> 1
        return cnt
# 		return bin(x^y).count('1')
