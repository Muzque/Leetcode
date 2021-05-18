"""
https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3731/
"""
"""
335 / 335 test cases passed.
Status: Accepted
Runtime: 176 ms
Memory Usage: 15.3 MB
"""
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        chance = True
        for i in range(1, len(nums)):
            if nums[i] >= nums[i-1]:
                continue
            if not chance:
                return False
            if (i == 1) or (nums[i] >= nums[i-2]):
                nums[i-1] = nums[i]
            else:
                nums[i] = nums[i-1]
            chance = False
        return True
            
            
        
