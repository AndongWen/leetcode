'''假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。'''
'''思路：
		1.对元素为0的区域进行判断，左边为0，右边也为0时，此处可以插花，
		同时需要将此处的值改为1，方便后续的操作。但是两个边界的判断时
		需要设置两个隐形的0
		2.判断连续的0区间的长度l:
		l<3:不能插花
		l为奇数：l//2
		l为偶数：l//2-1
		但是无法应用两边界为0时不可以这么判断，所以需要补0'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		'''思路1'''
        count = 0
        m = len(flowerbed)
        for i in range(m):
            if count >= n:
                return True 
            if flowerbed[i] == 1:
                continue
            pre = 0 if i == 0 else flowerbed[i-1]
            next = 0 if i == m-1 else flowerbed[i+1]
            if pre == 0 and next == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n # 不可以直接返回False，因为可能在最后一个位置插花

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		'''思路2'''
        count = 0
        flowerbed.insert(0, 0)
        flowerbed.append(0) # 相当于第二次遍历
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 1
            else:
                l = 0
                while i < len(flowerbed) and flowerbed[i] == 0:
                    l += 1
                    i += 1
                if l > 2:
                    if l%2 ==1:
                        count += l//2
                    else:
                        count += l//2 - 1
        return count >= n
