'''693交替位二进制数：给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等'''
'''思路：如ｎ是1,0交替的，那么temp=n^(n+1)一定全为1,则temp就是十进制下的2^N-1,
	移动过去就得到了temp+1=2^N,就是N+1位的二进制数，第一位为１，其余为０
	则temp&(temp+1)一定为０'''
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp = n^(n>>1)
        return temp&(temp+1) == 0
