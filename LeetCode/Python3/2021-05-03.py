"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3730/
"""
"""
53 / 53 test cases passed.
Status: Accepted
Runtime: 40 ms
Memory Usage: 14.3 MB
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for idx in range(1, len(nums)):
            nums[idx] += nums[idx-1]
        return nums
