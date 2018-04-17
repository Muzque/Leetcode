class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for j in range(0, len(nums)):
            hash_n = target - nums[j]
            nums2 = nums[j+1:]
            if hash_n in nums2:
                i = nums2.index(hash_n)+j+1
                break
        return [j, i]