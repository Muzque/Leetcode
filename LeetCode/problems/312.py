"""
312. Burst Balloons
Hard

You are given n balloons, indexed from 0 to n - 1.
Each balloon is painted with a number on it represented by an array nums.
You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.
"""
testcases = [
    {
        'input': {
            'nums': [3, 1, 5, 8]
        },
        'output': 167
    },
    {
        'input': {
            'nums': [9, 76, 64, 21, 97, 60],
        },
        'output': 1086136
    },
]

from lib import run_tests
from typing import List


def main():
    kls = Solution()
    run_tests(
        testcases=testcases,
        function=kls.maxCoins,
    )


class Solution(object):
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for _ in nums]
        print(nums)
        for i in range(len(nums) - 3, -1, -1):
            for j in range(i + 2, len(nums)):
                print(i, j)
                dp[i][j] = max([dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j] for k in range(i + 1, j)])
                print(dp)
        return dp[0][len(nums) - 1]
