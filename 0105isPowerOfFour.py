'''342给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。'''
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<0 or num&(num-1):
            return False    # 非2得幂
        return num%3 == 1 # 4 = 3+1  
		# (3+1)^N展开除了１＊１外，其余每个都有３,此规律可以扩展
