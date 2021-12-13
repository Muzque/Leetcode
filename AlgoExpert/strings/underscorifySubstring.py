"""

"""
testcases = [
    {
        'input': {
            "string": "testthis is a testtest to see if testestest it works",
            "substring": "test"
        },
        'output': '_test_this is a _testtest_ to see if _testestest_ it works',
    },
    {
        'input': {
            "string": "ttttttttttttttbtttttctatawtatttttastvb",
            "substring": "ttt"
        },
        'output': '_tttttttttttttt_b_ttttt_ctatawta_ttttt_astvb'
    },
    {
        'input': {
            "string": "this is a test to see if it works and test",
            "substring": "test"
        },
        'output': 'this is a _test_ to see if it works and _test_'
    },
    {
        'input': {
            "string": "abababababababababababababaababaaabbababaa",
            "substring": "a"
        },
        'output': '_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_a_b_aa_b_a_b_aaa_bb_a_b_a_b_aa_'
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=underscorifySubstring,
    )


def cut_recursive_string(i, string, substring, ret):
    span = len(substring)
    if i+span > len(string) or span == 0:
        return ret
    cut = string[i:i+span]
    if cut == substring:
        ret += substring
        return cut_recursive_string(i+span, string, substring, ret)
    return ret


def find_recursive_string(i, string, substring, ret):
    updated = cut_recursive_string(i, string, substring, ret)
    if len(updated) == len(ret):
        return updated
    return cut_recursive_string(i+len(updated), string, substring[1:], updated)


def underscorifySubstring(string, substring):
    ret = ''
    i = 0
    while i < len(string):
        r = find_recursive_string(i, string, substring, '')
        if r:
            ret += f'_{r}_'
            i += len(r)
        else:
            ret += string[i]
            i += 1
    return ret

