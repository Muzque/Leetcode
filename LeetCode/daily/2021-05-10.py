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


# Avg: 284.52
class Solution3:
    def countPrimes(self, n: int) -> int:
        ret = 0
        cache = dict((i, True) for i in range(2, n))
        for num, check in cache.items():
            if check is True:
                ret += 1
                times = math.ceil(n / num)
                for i in range(2, times):
                    cache[num*i] = False
        return ret


"""
21 / 21 test cases passed.
Status: Accepted
Runtime: 5196 ms
Memory Usage: 389.2 MB
"""


# Avg: 262.93
class Solution4:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        ret = 1
        cache = dict((i, True) for i in range(2, n))
        for num in range(3, n, 2):
            if cache[num] is True:
                ret += 1
                times = math.ceil(n / num)
                for i in range(2, times):
                    cache[num*i] = False
        return ret


"""

21 / 21 test cases passed.
Status: Accepted
Runtime: 672 ms
Memory Usage: 91.9 MB
"""


# Avg: 20.78
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        cache = [True] * n
        cache[0] = cache[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if cache[i]:
                cache[i*i:n:i] = [False] * len(cache[i*i:n:i])
        return sum(cache)
