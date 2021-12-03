"""

"""
testcases = [
    {
        'input': ('xyz', 2),
        'output': 'zab',
    },
    {
        'input': ('abc', 52),
        'output': 'abc'
    },
]


def caesarCipherEncryptor(string, key):
    arr = []
    for s in string:
        n = ord(s) + key % 26
        arr.append(n if n < 123 else 96 + (n - 122))
    return ''.join(chr(i) for i in arr)


if __name__ == '__main__':
    for tc in testcases:
        ret = caesarCipherEncryptor(*tc['input'])
        try:
            assert(ret == tc['output'])
        except Exception as e:
            print(ret)
            raise e
