"""

"""
testcases = [
    {
        'input': {
            'string': "AlgoExpert is the best!"
        },
        'output': 'best! the is AlgoExpert',
    },
    {
        'input': {
            'string': 'this      string     has a     lot of   whitespace'
        },
        'output': 'whitespace   of lot     a has     string      this'
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=reverseWordsInString,
    )


def reverseWordsInString(string):
    ret = ''
    pt = len(string)
    for i in range(len(string)-1, 0, -1):
        if (string[i] == ' ' and string[i-1] != ' ') or (string[i] != ' ' and string[i-1] == ' '):
            ret += string[i:pt]
            pt = i
    ret += string[:pt]
    return ret
