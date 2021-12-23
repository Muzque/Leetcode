testcases = [
    {
        'input': {
            "path": "/foo/../test/../test/../foo//bar/./baz"
        },
        'output': '/foo/bar/baz',
    },
    {
        'input': {
            "path": "../../foo/../../bar/baz"
        },
        'output': '../../../bar/baz',
    },
    {
        'input': {
            "path": "/../../foo/bar/baz"
        },
        'output': '/foo/bar/baz',
    },
    {
        'input': {
            "path": "/"
        },
        'output': '/',
    },
    {
        'input': {
            "path": "./.."
        },
        'output': '..'
    },
]


from lib import run_tests


def main():
    run_tests(
        testcases=testcases,
        function=shortenPath,
    )


"""
def shortenPath(path):
    stack = []
    is_abs = path[0] == '/'
    for p in path.split('/'):
        if (is_abs and len(stack) == 0 and p == '..') or p in ('.', ''):
            continue
        if len(stack) == 0:
            stack.append(p)
        elif p == '..' and stack[-1] != '..':
            stack.pop()
        else:
            stack.append(p)
    result = '/'.join(stack) or '/'
    return '/' + result if is_abs and result[0] != '/' else result
"""


def shortenPath(path):
    stack = []
    if path[0] == '/':
        stack.append('')
    for p in path.split('/'):
        if (stack and stack[-1] == '' and p == '..') or p in ('.', ''):
            continue
        if len(stack) == 0:
            stack.append(p)
        elif p == '..' and stack[-1] != '..':
            stack.pop()
        else:
            stack.append(p)
    return '/'.join(stack) or '/'
