"""

"""
testcases = [
    {
        'input': "AlgoExpert is the best!",
        'output': 'best! the is AlgoExpert',
    },
    {
        'input': 'this      string     has a     lot of   whitespace',
        'output': 'whitespace   of lot     a has     string      this'
    },
]


def reverseWordsInString(string):
    ret = ''
    pt = len(string)
    for i in range(len(string)-1, 0, -1):
        if (string[i] == ' ' and string[i-1] != ' ') or (string[i] != ' ' and string[i-1] == ' '):
            ret += string[i:pt]
            pt = i
    ret += string[:pt]
    return ret


if __name__ == '__main__':
    for tc in testcases:
        ret = reverseWordsInString(tc['input'])
        assert(ret == tc['output'])
