'''231给定一个整数，编写一个函数来判断它是否是 2 的幂次方。'''
import collections as coll

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
#        c = str(bin(n))
#        cnt = coll.Counter(c)
#        return cnt['1'] == 1 and n >0
        return n>0 and n&(n-1) == 0
