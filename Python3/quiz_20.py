class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        else:
            s = map(ord, s)
            ls = []
            for w in s:
                if w in [40, 91, 123]:
                    ls.append(w)
                elif ls and ls.pop() // 10 == w // 10:
                    continue
                else:
                    return False
            return len(ls) == 0


# def isValid(s):
#     stack, match = [], {')': '(', ']': '[', '}': '{'}
#     for ch in s:
#         if ch in match:
#             if not (stack and stack.pop() == match[ch]):
#                 return False
#         else:
#             stack.append(ch)
#     return not stack
