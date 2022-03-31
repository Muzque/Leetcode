testcases = [
    {
        'input': {
            "array": [45, 61, 71, 72, 73, 0, 1, 21, 33, 37],
            "target": 33
        },
        'output': 8
    },
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=shiftedBinarySearch,
    )


def shiftedBinarySearch(array, target):
    # Write your code here.
    pass
