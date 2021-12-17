testcases = [
    {
        'input': {
            "array": [1, 0, 0, -1, -1, 0, 1, 1],
            "order": [0, 1, -1]
        },
        'output': [0, 0, 0, 1, 1, 1, -1, -1],
    }
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=threeNumberSort
    )


def threeNumberSort(array, order):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] != array[j-1] and (
                array[j] == order[0] or
                (array[j] == order[1] and array[j-1] == order[2])):
            array[j], array[j-1] = array[j-1], array[j]
            j -= 1
    return array
