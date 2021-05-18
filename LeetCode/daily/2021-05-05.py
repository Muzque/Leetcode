"""
Jump Game II
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3732/
"""
"""
92 / 92 test cases passed.
Status: Accepted
Runtime: 28 ms
Memory Usage: 14.3 MB
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        cnt = 0
        idx = 0
        final = len(nums) - 1
        while idx < final:
            jump = nums[idx]
            if idx + jump >= final:
                return cnt + 1
            max_val = nums[idx+1] + 1
            bound = min(idx+jump+1, final)
            for i in range(idx+1, bound):
                if nums[i] > 0 and i + nums[i] >= max_val:
                    max_val = i+nums[i]
                    idx = i
            cnt += 1
        return cnt
        
