'''问题描述：对于给定的整数 n, 如果n的k（k>=2）进制数的所有数位全为1，
则称 k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制'''
class Solution(object):
	def smallgoodbase1(self, n):
		'''暴力解法，会超时'''
		i, j = 2, 0
		while True:
			sum = (pow(i, j)-1)/(k-1)
			if sum < n:
				j += 1
			elif sum == n:
				return str(i)
			else:
				i += 1
				j = 0
	
	def smallgoodbase2(self,n):
		'''二分法查找k:
			思路分析： 设n的最小好进制为k，转化为k进制后的字符串为"111…11"，
			这里的’1’分别代表这不同的权。
			进而n可以转化为 n == km-1 + km-2 + k m-3 + … + k1 + k0 （其中m待
            定，是一个常数，正好表示k进制中‘1’的个数，即转换为k进制的后的字
            符串的长度）不难发现这就是一个等比数列，根据等比数列的求和公式
			，可知 n == (km - 1) / (k - 1)，由于题目中要求进制k尽量的小，那	
			么根据求和公式知需要m尽可能的大（转换k进制后1的个数尽量多）。因
			为（k>=2），	所以m的最大值为 m = log2(num+1)
			并且由于n的取值范围是 [3, 10^18]，即m的最小值是2。'''
	 	n = int(n)
        m = int(math.log2(n+1))
#       for i in range(m, 1, -1):
		while m >= 2:
            left = 2
            right = int(pow(n, 1/(m-1))+1) # 由于采用二分法查找，下面的条件中不包含等号，左右right必须大于可能的k值
            while left < right:
                sum = 0
                mid = left + (right-left)//2
                for i in range(m):
                    sum = sum*mid + 1
                if sum < n:
                    left = mid +1
                elif sum == n:
                    return str(mid)
                else:
                    right = mid
			m -= 1
        return str(n-1)

    def smallestGoodBase3(self, n: str) -> str:
        n = int(n)
        m = int(math.log2(n+1))
        cat = set()
        p = 2
        cat.add(2)
        for i in range(m, 2, -1):
            p = int(pow(n, 1/(i-1))) # p为实实在在的k值，不需要加1
            cat.add(p)
        for i in cat:
            if n%i == 1:
                h = n*i-n+1
                t = i
                while t<h:
                    t = t*i
                    if t ==h:
                        return str(i)
        return str(n-1)
