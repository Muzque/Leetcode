"""
368. Largest Divisible Subset
"""
testcases = [
    {
        'input': ([1, 2, 3]),
        'output': [1, 2]
    },
    {
        'input': ([1, 2, 4, 8]),
        'output': [1, 2, 4, 8],
    },
    {
        'input': ([1, 2, 3, 4, 8, 9, 27, 81]),
        'output': [1, 3, 9, 27, 81],
    },
    {
        'input': ([3, 4, 16, 8]),
        'output': [4, 8, 16],
    },
    {
        'input': ([4, 8, 10, 240]),
        'output': [4, 8, 240],
    }
]

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        h = len(nums)
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(h):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j])+1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        return max(dp, key=len)


if __name__ == '__main__':
    sol = Solution()
    for idx, case in enumerate(testcases):
        print(f'Testcase ({idx+1}):')
        ret = sol.largestDivisibleSubset(case['input'])
        try:
            assert(ret == case['output'])
        except:
            print(f'Expected: {case["output"]}, but got {ret}')
