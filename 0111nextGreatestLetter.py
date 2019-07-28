'''744寻找比目标字母大的最小字母:
	给定一个只包含小写字母的有序数组letters 和一个目标字母 target，
	寻找有序数组里面比目标字母大的最小字母。
	数组里字母的顺序是循环的。举个例子，如果目标字母target = 'z' 
	并且有序数组为 letters = ['a', 'b']，则答案返回 'a'.'''
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
		# 二分法
        if not letters:
            return None
        n = len(letters)
        l, h = 0, n-1
        while l <= h:
            m = l + (h-l)//2
            if letters[m] <= target:
                l = m+1
            else:
                h = m-1
        
        return letters[l] if l < n else letters[0]
