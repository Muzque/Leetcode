"""

"""
testcases = [
    {
        'input': 'AAAAAAAAAAAAABBCCCCDD',
        'output': '9A4A2B4C2D',
    },
]


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


if __name__ == '__main__':
    for tc in testcases:
        ret = runLengthEncoding(tc['input'])
        assert(ret == tc['output'])
