"""
410. Split Array Largest Sum
Hard

Given an array nums which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.



Example 1:
    Input: nums = [7,2,5,10,8], m = 2
    Output: 18
    Explanation:
        There are four ways to split nums into two subarrays.
        The best way is to split it into [7,2,5] and [10,8],
        where the largest sum among the two subarrays is only 18.

Example 2:
    Input: nums = [1,2,3,4,5], m = 2
    Output: 9

Example 3:
    Input: nums = [1,4,4], m = 3
    Output: 4


Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 106
    1 <= m <= min(50, nums.length)
"""
testcases = [
    {
        'input': {
            'nums': [7, 2, 5, 10, 8],
            'm': 2,
        },
        'output': 18,
    },
    {
        'input': {
            'nums': [1, 2, 3, 4, 5],
            'm': 2,
        },
        'output': 9,
    },
    {
        'input': {
            'nums': [1, 4, 4],
            'm': 3,
        },
        'output': 4,
    },
]

from typing import List
from lib import run_tests


# 59ms 50.91% | 14MB 37.77%
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            current, cnt = 0, 1
            for num in nums:
                if current + num <= mid:
                    current += num
                else:
                    current = num
                    cnt += 1
            if cnt > m:
                left = mid + 1
            else:
                right = mid
        return right


def main():
    sol = Solution()
    run_tests(
        testcases=testcases,
        function=sol.splitArray,
    )
