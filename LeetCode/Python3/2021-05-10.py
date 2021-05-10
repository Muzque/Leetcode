testcases = {
    '1': ([10], 4),
    '2': ([0], 0),
    '3': ([1], 0),
    '4': ([499979], 41537),
    '5': ([5], 2),
    '6': ([1500000], 114155),
    '7': ([100], 25),
}

import math


# TLE 4
class Solution1:
    def countPrimes(self, n: int) -> int:
        ret = 0
        for i in range(2, n):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                ret += 1
        return ret


# TLE 6
class Solution2:
    def countPrimes(self, n: int) -> int:
        ret = 0
        if n > 2:
            ret += 1
        for i in range(2, n):
            top = math.ceil(i ** 0.5)
            for j in range(2, top+1):
                if i % j == 0:
                    break
            else:
                ret += 1
        return ret


"""
21 / 21 test cases passed.
Status: Accepted
Runtime: 6396 ms
Memory Usage: 389.3 MB
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        ret = 0
        cache = dict((i, True) for i in range(2, n))
        for num, check in cache.items():
            times = math.ceil(n/num)
            if check is True:
                ret += 1
                for i in range(2, times):
                    cache[num*i] = False
        return ret
