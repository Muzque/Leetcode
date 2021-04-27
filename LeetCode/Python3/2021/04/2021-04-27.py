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
