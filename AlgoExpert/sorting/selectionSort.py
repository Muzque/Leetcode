testcases = [
    {
        'input': {
            "array": [8, 5, 2, 9, 5, 6, 3]
        },
        'output': [2, 3, 5, 5, 6, 8, 9]
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=selectionSort,
    )


def selectionSort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
