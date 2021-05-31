"""
Maximum Gap
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3761/
"""
"""
Given an integer array nums, return the maximum difference between two 
successive elements in its sorted form. If the array contains less than two 
elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra 
space.

 

Example 1:
Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) 
has the maximum difference 3.

Example 2:
Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 109
"""
testcases = {
    '1': ([[3, 6, 9, 1]], 3),
    '2': ([[10]], 0),
}

from typing import List


"""
17 / 17 test cases passed.
Status: Accepted
Runtime: 84 ms
Memory Usage: 15.1 MB
"""


# Loop avg. cost: 0.0037431716918945312 ms
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for i in range(1, len(nums)):
            result = max(result, nums[i] - nums[i-1])
        return result
