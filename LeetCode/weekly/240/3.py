"""
1856. Maximum Subarray Min-Product
https://leetcode.com/contest/weekly-contest-240/problems/maximum-subarray-min-product/
"""
from typing import List

testcases = {
    '1': ([[1, 2, 3, 2]], 14),
}


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
class Solution2:
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


"""
42 / 42 test cases passed.
Status: Accepted
Runtime: 1080 ms
Memory Usage: 25.8 MB
Submitted: 0 minutes ago
"""


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        mod = int(1e9 + 7)
        stack = [(-1, 0)]
        running_sum = running_max = 0
        nums.append(0)
        for num in nums:
            while stack[-1][0] >= num:
                min_value, _ = stack.pop()
                running_max = max(running_max,
                                  min_value * (running_sum - stack[-1][1]))
            running_sum += num
            stack.append((num, running_sum))
        return running_max % mod


"""
inputs = [1, 2, 3, 2]
answer = 14
---------------------------
* Init
    nums = [1, 2, 3, 2, 0]
    stack = [(-1, 0)]
    running_sum = 0
    running_max = 0

*   num = 1
    running_sum = 0 + 1 = 1
    stack = [(-1, 0), (1, 1)]

*   num = 2
    running_sum = 1 + 2 = 3
    stack = [(-1, 0), (1, 1), (2, 3)]

*   num = 3
    running_sum = 3 + 3 = 6
    stack = [(-1, 0), (1, 1), (2, 3), (3, 6)]

*   num = 2         
    # breaks the monotonic and pop out last item
    min_value = 3
    stack = [(-1, 0), (1, 1), (2, 3)]
    # calculate max: previous_value * (diff sum)
    max_value = 3 * (6 - 3) = 9
    running_max = 9
    ...
    # still breaks the monotonic and pop out last item
    min_value = 2
    stack = [(-1, 0), (1, 1)]
    # calculate max: previous_value * (diff sum)
    max_value = 2 * (6 - 1) = 10
    running_max = 10
    ...
    running_sum = 6 + 2 = 8
    stack = [(-1, 0), (1, 1), (2, 8)]
    
*   num = 0
    # breaks the monotonic
    min_value = 2
    stack = [(-1, 0), (1, 1)]
    # calculate max: previous_value * (diff sum)
    max_value = 2 * (8 - 1) = 14
    running_max = 14
    ...
    # still breaks the monotonic
    min_value = 1
    stack = [(-1, 0)]
    # calculate max: previous_value * (diff sum)
    max_value = 1 * (8 - 0) = 8
    ...
    running_sum = 8 + 0 = 8
    stack = [(-1, 0), (0, 8)]    
"""
"""
stacks                                   num running_max
    [(-1, 0)]                           |   |
    [(-1, 0), (1, 1)]                   | 1 |
    [(-1, 0), (1, 1), (2, 3)]           | 2 |
    [(-1, 0), (1, 1), (2, 3), (3, 6)]   | 3 |
    [(-1, 0), (1, 1), (2, 3)]           | 2 | 3 * (6 - 3) = 9
    [(-1, 0), (1, 1)]                   | 2 | 2 * (6 - 1) = 10
    [(-1, 0), (1, 1), (2, 8)]           | 2 |
    [(-1, 0), (1, 1)]                   | 0 | 2 * (8 - 1) = 14
    [(-1, 0)]                           | 0 | 1 * (8 - 0) = 8
    [(-1, 0), (0, 8)]                   | 0 |
"""
"""
nums        = [1, 2, 3, 2, 0]
running_sum = [1, 3, 6, 8, 8]
max_value   = [-, -, -, 9, 10, 14, 8]
"""
