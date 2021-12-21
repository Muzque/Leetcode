testcases = [
    {
        'input': {
            "one": "algoexpert",
            "three": "your-algodream-expertjob",
            "two": "your-dream-job"
        },
        'output': True,
    },
]


from lib import run_tests


def main():
    run_tests(testcases, interweavingStrings)


def interweavingStrings(one, two, three):
    if len(three) == 0:
        return len(one) == len(two) == 0
    left , right = False, False
    if one and one[0] == three[0]:
        left = interweavingStrings(one[1:], two, three[1:])
    if two and two[0] == three[0]:
        right = interweavingStrings(one, two[1:], three[1:])
    return left or right
