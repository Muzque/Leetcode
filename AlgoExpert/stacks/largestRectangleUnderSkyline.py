testcases = [
    {
        'input': {
            "buildings": [1, 3, 3, 2, 4, 1, 5, 3, 2]
        },
        'output': 9
    },
    {
        'input': {
            "buildings": [4, 4, 4, 2, 2, 1]
        },
        'output': 12
    },
    {
        'input': {
            "buildings": [1, 3, 3, 2, 4, 1, 5, 3]
        },
        'output': 8
    },
    {
        'input': {
            "buildings": []
        },
        'output': 0
    },
    {
        'input': {
            "buildings": [1, 3, 3, 2, 4, 1, 1, 9]
        },
        'output': 9
    },

]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=largestRectangleUnderSkyline,
    )


"""
def largestRectangleUnderSkyline(buildings):
    result = 0
    for i in range(len(buildings)):
        candidates = [buildings[i]] + [(i-j+1) * min(buildings[j:i+1]) for j in range(i)]
        max_local = max(candidates)
        result = max(result, max_local)
    return result
"""


def largestRectangleUnderSkyline(buildings):
    result = 0
    for i in range(len(buildings)):
        height = buildings[i]
        right, left = i, i
        while left > 0 and buildings[left-1] >= height:
            left -= 1
        while right < len(buildings) - 1 and buildings[right+1] >= height:
            right += 1
        area = (right - left + 1) * height
        result = max(result, area)
    return result
