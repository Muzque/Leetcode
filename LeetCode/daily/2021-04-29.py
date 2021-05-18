"""
88 / 88 test cases passed.
Status: Accepted
Runtime: 88 ms
Memory Usage: 15.5 MB
"""

class Solution:
    def find_left(self, nums, target, left, right):
        if left >= right - 1:
            if nums[left] == target:
                return left
            return left + 1
        pt = (left + right) // 2
        if nums[pt] < target:
            return self.find_left(nums, target, pt, right)
        return self.find_left(nums, target, left, pt)
    
    def find_right(self, nums, target, left, right):
        if left >= right - 1:
            if nums[right] == target:
                return right
            return right - 1
        pt = (left + right) // 2
        if nums[pt] > target:
            return self.find_right(nums, target, left, pt)
        return self.find_right(nums, target, pt, right)
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]
        left, right = 0, len(nums) - 1
        l = self.find_left(nums, target, left, right)
        r = self.find_right(nums, target, left, right)
        if r < l:
            return [-1, -1]
        else:
            return [l, r]
        
