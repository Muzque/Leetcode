"""
An array A consisting of N integers is given. An inversion is a pair of indexes (P, Q) such that P < Q and A[Q] < A[P].

Write a function:

def solution(A)

that computes the number of inversions in A, or returns −1 if it exceeds 1,000,000,000.

For example, in the following array:

 A[0] = -1 A[1] = 6 A[2] = 3
 A[3] =  4 A[4] = 7 A[5] = 4
there are four inversions:

   (1,2)  (1,3)  (1,5)  (4,5)
so the function should return 4.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""

testcases = [
    {
        'input': [-1, 6, 3, 4, 7, 4],
        'output': 4,
    },
]


# Task Score: 63%
# Correctness: 100% & Performance: 20%
# Time: O(N**2)
def solution(A):
    ret = 0
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                ret += 1
    if ret > 1000000000:
        return -1
    return ret


if __name__ == '__main__':
    for tc in testcases:
        ret = solution(tc['input'])
        assert(ret == tc['output'])
