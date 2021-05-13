"""
1854. Maximum Population Year
https://leetcode.com/contest/weekly-contest-240/problems/maximum-population-year/
"""
from typing import List


"""
52 / 52 test cases passed.
Status: Accepted
Runtime: 44 ms
Memory Usage: 14.3 MB
"""


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        b = 1950
        arr = [0] * 101
        max_val = 0
        max_year = 2050
        for log in logs:
            for n in range(log[0], log[1]):
                arr[n - b] += 1
                if arr[n - b] > max_val:
                    max_val = arr[n - b]
                    max_year = n
                elif arr[n - b] == max_val and n < max_year:
                    max_year = n
        return max_year
