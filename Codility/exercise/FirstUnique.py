"""
A non-empty array A consisting of N integers is given.
The unique number is the number that occurs exactly once in array A.

For example, given:

  A[0] = 1
  A[1] = 4
  A[2] = 3
  A[3] = 3
  A[4] = 1
  A[5] = 2
There are two unique numbers (4 and 2 occur exactly once).
The first one is 4 in position 1 and the second one is 2 in position 5.
The function should return 4 because it is unique number with the lowest position.

Return −1. There is no unique number in A
"""
testcases = [
    {
        'input': [4, 10, 5, 4, 2, 10],
        'output': 5,
    },
    {
        'input': [1, 4, 3, 3, 1, 2],
        'output': 4,
    },
    {
        'input': [6, 4, 4, 6],
        'output': -1,
    },
]


# Task Score: 100%
# Correctness: 100%
# Performance: 100%
# Time: O(n * log(n))
def solution(A):
    cached = {}
    for num in A:
        cached[num] = cached.get(num, 0) + 1
    for k, v in cached.items():
        if v == 1:
            return k
    return -1


if __name__ == '__main__':
    for tc in testcases:
        ret = solution(tc['input'])
        assert(ret == tc['output'])
