"""
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct
indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

"""
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cached = {}
        for i, num in enumerate(nums):
            if num not in cached:
                cached[num] = i
            else:
                j = cached[num]
                if abs(i - j) <= k:
                    return True
                cached[num] = i
        return False
