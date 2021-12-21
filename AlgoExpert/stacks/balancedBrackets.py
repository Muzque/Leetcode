def balancedBrackets(string):
    cached = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    allowed = cached.values()
    stacks = []
    for s in string:
        if s in cached:
            if len(stacks) == 0:
                return False
            pair = stacks.pop()
            if cached[s] != pair:
                return False
        elif s in allowed:
            stacks.append(s)
    return len(stacks) == 0
