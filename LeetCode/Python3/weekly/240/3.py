"""
1856. Maximum Subarray Min-Product
https://leetcode.com/contest/weekly-contest-240/problems/maximum-subarray-min-product/
"""
from typing import List


# TLE 20/42
class Solution1:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        h = len(nums)
        max_val = 0
        for j in range(h):
            for i in range(j, h):
                val = sum(nums[j:i+1]) * min(nums[j:i+1])
                if val > max_val:
                    max_val = val
        return max_val


# TLE 23/42
class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        h = len(nums)
        max_val = 0
        for j in range(h):
            base = 0
            min_val = float('inf')
            for i in range(j, h):
                base += nums[i]
                if nums[i] < min_val:
                    min_val = nums[i]
                val = base * min_val
                if val > max_val:
                    max_val = val
        return max_val % mod
