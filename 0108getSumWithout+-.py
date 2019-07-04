'''不使用运算符 + 和 -，计算两整数 a 、b 之和。'''
'''异或表示加的结果，与后右移一位表示仅为的结果，反复迭代直到进位的值为０'''
'''在 Python 中，整数不是 32 位的，也就是说你一直循环左移并不会存在溢出的现象，这就需要我们手动对 Python 中的整数进行处理，手动模拟 32 位 INT 整型。
。'''
class Solution:
    def getSum(self, a: int, b: int) -> int:
		# 2^32
		mask = 0x100000000
		MAX_INT = 0x7fffffff
		MIN_INT = MAX_INT + 1
		while b != 0:
			carry = (a&b)<<1
			# 将范围限制在[0, 2^32-1]范围内
			a = (a^b)%mask
			b = (carry)%mask
			
		return a if a <= MAX_INT else ~((a%MIN_INT)^MAX_INT) # 简言之，就是取模后最高位不动

