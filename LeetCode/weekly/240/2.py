"""
Maximum Distance Between a Pair of Values
https://leetcode.com/contest/weekly-contest-240/problems/maximum-distance-between-a-pair-of-values/
"""
from typing import List


# TLE
class Solution1:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_distance = 0
        for j in range(len(nums1)):
            for i in range(len(nums2)):
                dx = nums2[i] - nums1[j]
                if dx < 0:
                    break
                dh = i - j
                if dh > max_distance:
                    max_distance = dh
        return max_distance


# TLE
class Solution2:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        max_distance = 0
        for j in range(len(nums1)):
            for i in range(j, len(nums2)):
                dx = nums2[i] - nums1[j]
                if dx < 0:
                    break
                dh = i - j
                if dh > max_distance:
                    max_distance = dh
        return max_distance


"""
32 / 32 test cases passed.
Status: Accepted
Runtime: 1120 ms
Memory Usage: 32.2 MB
"""


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        dj = len(nums1)
        di = len(nums2)
        max_distance = 0
        for j in range(dj):
            s = max_distance + j
            for i in range(s, di):
                dx = nums2[i] - nums1[j]
                if dx < 0:
                    break
                dh = i - j
                if dh > max_distance:
                    max_distance = dh
        return max_distance
