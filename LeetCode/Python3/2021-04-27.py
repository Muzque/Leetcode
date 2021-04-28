"""
21038 / 21038 test cases passed.
Status: Accepted
Runtime: 72 ms
Memory Usage: 14.4 MB
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def rec(power: int, num: int):
            if num % 3 == 0:
                return rec(power+1, num/3)
            return power, num
        if n == 0:
            return False
        power, left = rec(0, n)
        return left == 1.0

"""
21038 / 21038 test cases passed.
Status: Accepted
Runtime: 64 ms
Memory Usage: 13.9 MB
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0
