"""

"""
testcases = [
    {
        'input': {
            'string': 'xyz',
            'key': 2
        },
        'output': 'zab',
    },
    {
        'input': {
            'string': 'abc',
            'key': 52
        },
        'output': 'abc'
    },
]

from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=caesarCipherEncryptor,
    )


def caesarCipherEncryptor(string, key):
    arr = []
    for s in string:
        n = ord(s) + key % 26
        arr.append(n if n < 123 else 96 + (n - 122))
    return ''.join(chr(i) for i in arr)
