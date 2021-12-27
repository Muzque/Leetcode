"""
2122. Recover the Original Array
Difficulty:Hard

Alice had a 0-indexed array arr consisting of n positive integers.
She chose an arbitrary positive integer k and created two new 0-indexed integer arrays lower and
higher in the following manner:
    lower[i] = arr[i] - k, for every index i where 0 <= i < n
    higher[i] = arr[i] + k, for every index i where 0 <= i < n

Unfortunately, Alice lost all three arrays.
However, she remembers the integers that were present in the arrays lower and higher, but not the array each integer
belonged to.
Help Alice and recover the original array.

Given an array nums consisting of 2n integers, where exactly n of the integers were present in lower and the remaining
in higher, return the original array arr. In case the answer is not unique, return any valid array.

Note: The test cases are generated such that there exists at least one valid array arr.
"""
testcases = [
    {
        'input': {
            'nums': [2, 10, 6, 4, 8, 12],
        },
        'output': [3, 7, 11]
    },
    {
        'input': {
            'nums': [1, 1, 3, 3],
        },
        'output': [2, 2]
    },
    {
        'input': {
            'nums': [5, 435],
        },
        'output': [220]
    },
    {
        'input': {
            'nums': [0, 2, 99, 103, 255, 251, 10, 6, 6, 4],
        },
        'output': [2, 4, 8, 101, 253]
    },
]


from typing import List
from lib import run_tests
from collections import Counter


def main():
    kls = Solution()
    run_tests(
        testcases=testcases,
        function=kls.recoverArray,
    )


# 372ms PR100 | 14.8MB PR92.86
class Solution:

    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        cached = Counter(nums)
        for i in range(1, len(nums)):
            diff = nums[i] - nums[0]
            if diff and diff & 1 == 0:
                result = []
                freq = cached.copy()
                for num, cnt in freq.items():
                    if cnt:
                        if freq[num+diff] < cnt:
                            break
                        result.extend([num+diff//2]*cnt)
                        freq[num+diff] -= cnt
                else:
                    return result
