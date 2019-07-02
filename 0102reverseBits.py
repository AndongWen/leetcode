'''190颠倒二进制位:颠倒给定的 32 位无符号整数的二进制位。'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
		res = 0
		for i in range(32):
			res <<= 1
			res |= n&1
			n >>= 1

		return res


		return int(bin(n)[2:].zfill(32)[::-1], 2)
