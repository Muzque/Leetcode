"""
Super Palindromes
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3736/
"""
testcases = {
    '1': (["4", "1000"], 4),
    '2': (["1", "2"], 1),
    '3': (["40000000000000000", "50000000000000000"], 2),
    '4': (['123456', '123456789'], 8),
    '5': (['1000', '10000'], 0),
    '6': (['10000', '100000'], 5),
    '7': (['200000', '3000000'], 2),
    '8': (['6000000', '70000000'], 0),
    '9': (['10000000', '50000000'], 0),
    '10': (['400000000', '500000000'], 2),
    '11': (['111', '231'], 1),
    '12': (['1', '999999999999999999'], 70),
}

import math


# TLE 3
class Solution1:
    def is_palindrome(self, n):
        if n < 10: return True
        word = str(n)
        mid = len(word) // 2
        return word[:mid] == word[:len(word) - mid - 1:-1]

    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = math.ceil(int(left) ** 0.5)
        right = math.ceil(int(right) ** 0.5)
        cnt = 0
        for num in range(left, right):
            if self.is_palindrome(num):
                if self.is_palindrome(num ** 2):
                    cnt += 1
        return cnt


"""
49 / 49 test cases passed.
Status: Accepted
Runtime: 1104 ms
Memory Usage: 40.6 MB
"""


# Avg. 102.99
class Solution2:

    def _get_possibility(self, bot, top):
        left, right = len(str(bot)), len(str(top))
        even = [['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']]
        while len(even[-1][0])+2 <= right:
            tmp = [f'{i}{a}{i}' for a in even[-1] for i in range(10)]
            even.append(tmp)
        odd = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
        while len(odd[-1][0])+2 <= right:
            tmp = [f'{i}{a}{i}' for a in odd[-1] for i in range(10)]
            odd.append(tmp)
        ret = []
        for arr in even:
            ret += [int(n) for n in arr]
        for arr in odd:
            ret += [int(n) for n in arr]
        return ret

    def _is_palindrome(self, num: int) -> bool:
        s = str(num)
        h = len(s)
        mid = h // 2
        for i in range(mid):
            if s[i] != s[h-i-1]:
                return False
        return True

    def superpalindromesInRange(self, left: str, right: str) -> int:
        bot = math.ceil(int(left) ** 0.5)
        top = math.floor(int(right) ** 0.5)
        arr = self._get_possibility(bot, top)
        cnt = 0
        left, right = int(left), int(right)
        for n in arr:
            nn = n ** 2
            if right >= nn >= left and self._is_palindrome(nn):
                cnt += 1
        return cnt


"""
49 / 49 test cases passed.
Status: Accepted
Runtime: 1112 ms
Memory Usage: 40.7 MB
"""


# Avg cost: 98.84
class Solution3:

    def _get_possibility(self, bot, top):
        left, right = len(str(bot)), len(str(top))
        even = [['00', '11', '22', '33', '44', '55', '66', '77', '88', '99']]
        while len(even[-1][0])+2 <= right:
            tmp = [f'{i}{a}{i}' for a in even[-1] for i in range(10)]
            even.append(tmp)
        odd = [['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']]
        while len(odd[-1][0])+2 <= right:
            tmp = [f'{i}{a}{i}' for a in odd[-1] for i in range(10)]
            odd.append(tmp)
        ret = []
        for arr in even:
            ret += [int(n) for n in arr]
        for arr in odd:
            ret += [int(n) for n in arr]
        return ret

    def _is_palindrome(self, num: int) -> bool:
        s = str(num)
        h = len(s)
        mid = h // 2
        return s[:mid] == s[:h-mid-1:-1]

    def superpalindromesInRange(self, left: str, right: str) -> int:
        bot = math.ceil(int(left) ** 0.5)
        top = math.floor(int(right) ** 0.5)
        arr = self._get_possibility(bot, top)
        cnt = 0
        left, right = int(left), int(right)
        for n in arr:
            nn = n ** 2
            if right >= nn >= left and self._is_palindrome(nn):
                cnt += 1
        return cnt


"""
49 / 49 test cases passed.
Status: Accepted
Runtime: 88 ms
Memory Usage: 14.4 MB
"""

from itertools import product


# Avg cost: 25.30
class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        seen = set()
        for d in product(('0', '1', '2', '3'), repeat=5):
            num = "".join(d).rstrip('0')
            if not num:
                continue
            for n in (num[::-1] + num, num[::-1] + num[1:]):
                x = int(n) ** 2
                if x not in seen and left <= x <= right:
                    seen.add(x)
        return sum(str(x) == str(x)[::-1] for x in seen)
