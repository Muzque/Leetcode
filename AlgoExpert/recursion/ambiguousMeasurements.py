testcases = [
    {
        'input': {
            'measuringCups': [
                [200, 210],
                [450, 465],
                [800, 850]
            ],
            'low': 2100,
            'high': 2300
        },
        'output': True
    },
    {
        'input': {
            'measuringCups': [
                [200, 210],
                [450, 465],
                [800, 850]
            ],
            'low': 200,
            'high': 200
        },
        'output': False
    },
    {
        'input': {
            'measuringCups': [
                [200, 200],
                [450, 465],
                [800, 850]
            ],
            'low': 200,
            'high': 200
        },
        'output': True
    },
    {
        'input': {
            "high": 20,
            "low": 10,
            "measuringCups": [
                [200, 210]
            ]
        },
        'output': False
    },
    {
        'input': {
            "high": 2300,
            "low": 2100,
            "measuringCups": [
                [230, 240],
                [290, 310],
                [500, 515]
            ]
        },
        'output': True
    },
    {
        'input': {
            "high": 101,
            "low": 100,
            "measuringCups": [
                [1, 3],
                [2, 4],
                [5, 6]
            ]
        },
        'output': False
    },
    {
        'input': {
            "high": 12,
            "low": 10,
            "measuringCups": [
                [1, 3],
                [2, 4],
                [5, 6],
                [10, 20]
            ]
        },
        'output': True
    },
    {
        'input': {
            "high": 1050,
            "low": 1000,
            "measuringCups": [
                [50, 60],
                [100, 120],
                [20, 40],
                [10, 15],
                [400, 500]
            ]
        },
        'output': False
    },
    {
        'input': {
            "high": 200,
            "low": 200,
            "measuringCups": [
                [50, 65]
            ]
        },
        'output': False
    },
    {
        'input': {
            "high": 20,
            "low": 10,
            "measuringCups": [
                [15, 22]
            ]
        },
        'output': False
    }
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=ambiguousMeasurements,
    )


# O(low * high * n) time | O(low * high) space - where n is the number of measuring cups
def ambiguousMeasurements(measuringCups, low, high, cached=None):
    if cached is None:
        cached = {}
    key = f'{low}:{high}'
    if key in cached:
        return cached[key]
    if high <= 0:
        return False

    for cup in measuringCups:
        if cup[0] >= low and high >= cup[1]:
            cached[key] = True
            return True

        if ambiguousMeasurements(measuringCups, low-cup[0], high-cup[1], cached):
            cached[key] = True
            return True
    cached[key] = False
    return False
