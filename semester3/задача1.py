class Solution(object):
    def isHappy(self, n):
        while n >= 1:
            a = n
            n = 0
            while a > 0:
                n += (a % 10) ** 2
                a = a // 10
            if n == 1:
                return True
            if n == 4:
                return False
        
