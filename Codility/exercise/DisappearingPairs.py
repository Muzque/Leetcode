"""
Given a string S consisting of N characters,
returns any string that can result from a sequence of transformations as described above.

For example, given string S = "ACCAABBC" the function may return "AC",
because one of the possible sequences of transformations is as follows:

ACCAABBC -> ACCBBC -> ACCC -> AC

Finally, for string S = "BABABA" the function must return "BABABA", because no rules can be applied to string S

Write an efficient algorithm for the following assumptions:
    - the length of S is within the range [0..50,000];
    - string S consists only of the following characters: "A", "B" and/or "C".
"""
testcases = [
    {
        'input': 'ACCAABBC',
        'output': 'AC',
    },
    {
        'input': 'BABABA',
        'output': 'BABABA',
    },
]


# Task Score: 50%
# Correctness: 100%
# Performance: 0%
# Time: O(2 ** N)
def solution(S):
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            return solution(S[:i] + S[i+2:])
    return S


if __name__ == '__main__':
    for tc in testcases:
        ret = solution(tc['input'])
        assert(ret == tc['output'])
