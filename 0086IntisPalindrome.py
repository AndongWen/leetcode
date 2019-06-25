'''9回文数:判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）
	读都是一样的整数。'''

class solution:
    def ispalindrome(self, x: int) -> bool:
#        return str(x) == str(x)[::-1]
		# 依次取出数字的首位来进行判断
        if x < 0:
            return False
        div = 1
        while x//div >= 10:
            div *= 10
        while div > 1:
            left = x//div
            right = x%10
            if left != right:
                return False
            x = x%div//10
            div = div/100
        return True


class solution:
    def ispalindrome(self, x: int) -> bool:
	#　将数字后半段倒置与前半段对比，偶数两部分正好相等，奇数则有一个需要除10取整
		if x < 0 or ( x%10 == 0 and x != 0):
			return False
		r_x = 0
		while x > r_x:
			r_x = r_x * 10 + x%10
			x //= 10
		return x == r_x or x == r_x//10
