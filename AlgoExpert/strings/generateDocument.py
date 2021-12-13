"""

"""
testcases = [
    {
        'input': {
            'characters': "Bste!hetsi ogEAxpelrt x ",
            'document': "AlgoExpert is the Best!"
        },
        'output': True,
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=generateDocument,
    )


def count(string):
    cached = {}
    for s in string:
        cached[s] = cached.get(s, 0) + 1
    return cached


def generateDocument(characters, document):
    cached_c = count(characters)
    cached_d = count(document)
    for k, v in cached_d.items():
        r = cached_c.pop(k, 0)
        if r < v:
            return False
    return True
