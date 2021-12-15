testcases = [
    {
        'input': {
            "array": [8, 5, 2, 9, 5, 6, 3]
        },
        'output': [2, 3, 5, 5, 6, 8, 9],
    },
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=insertionSort,
    )


def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array
