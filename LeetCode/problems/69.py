"""
69. Sqrt(x)
Easy

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator,
such as pow(x, 0.5) or x ** 0.5.
"""


# 2865ms 8.94% | 14.2MB 69.9%
class Solution:
    def mySqrt(self, x: int) -> int:
        root = x // 2
        while root ** 2 > x:
            root //= 2
        while True:
            if (root+1) ** 2 > x:
                return int(root)
            root += 1


# 9386ms 5% | 14.2MB 41.09%
class Solution1:
    def mySqrt(self, x: int) -> int:
        for i in range(x+1):
            j = i ** 2
            if j == x:
                return i
            elif j > x:
                return i-1


# 48ms 41.76% | 14.2MB 69.90%
class Solution2:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            pt = (left + right) // 2
            if pt ** 2 == x:
                return pt
            if pt ** 2 > x:
                right = pt - 1
            else:
                left = pt + 1
        return right
