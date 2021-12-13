"""

"""
testcases = [
    {
        'input': {
            'string': 'AAAAAAAAAAAAABBCCCCDD'
        },
        'output': '9A4A2B4C2D',
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=runLengthEncoding,
    )


def runLengthEncoding(string):
    ret = ''
    count = 1
    word = string[0]
    for s in string[1:]:
        if s != word or count == 9:
            ret += f'{count}{word}'
            count = 1
            word = s
        else:
            count += 1
    ret += f'{count}{word}'
    return ret
