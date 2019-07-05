'''338比特位计数:
	给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回'''
class Solution:
    def countBits(self, num: int) -> List[int]:
		# 使用内置函数
        res = []
        for i in range(num+1):
            res.append(bin(i).count('1'))
           
        return res

class Solution:
    def countBits(self, num: int) -> List[int]:
		'''观察进而得出规律:
			0    0    0
			1	 1    1  0的答案+1
			2	10	  1  0的答案+1
			3   11    2  1的答案+1
			4  100    1  0的答案+1
			5  101	  2  1的答案+1
			6  110    2  2的答案+1
			7  111    3  3的答案+1
			8 1000    1  0的答案+1
			.......
			对于1xxxx的答案就是xxxx答案+1，所以可以由小数向大数递推'''
        res = [0]
        n = len(res)
        while n < num+1:
            for i in range(n):
                res.append(res[i]+1)
            n = len(res)

        return res[:num+1]

class Solution:
    def countBits(self, num: int) -> List[int]:
		'''i&(i-1)去掉i中最低的一位，所以i的答案就是i&(i-1)+1,同时i&(i-1)一定比i小
			也就是说计算i的时候，i&(i-1)一定已经计算过了'''
        res = [0] * (num+1)
        for i in range(1, num+1):
            res[i] = res[i&(i-1)] + 1
            
        return res

class Solution:
    def countBits(self, num: int) -> List[int]:
	'''i >> 1去掉i的最低位；因(i >> 1) < i，故result[i >> 1]已计算，因此i中1的个数为i >> 1中1的个数加最后一位1的个数，即为result[i >> 1] + (i & 1)'''
        res = [0] * (num+1)
        for i in range(1, num+1):
            res[i] = res[i>>1] + (i&1)
            
        return res
