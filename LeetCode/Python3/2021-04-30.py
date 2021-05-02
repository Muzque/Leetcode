"""
102 / 102 test cases passed.
Status: Accepted
Runtime: 20 ms
Memory Usage: 14.3 MB
"""
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if y > x:
            x, y = y, x
        hx = 10000 if x > 1 else 1
        hy = 10000 if y > 1 else 1
        result = set()
        for i in range(hx):
            a = x ** i
            if a > bound:
                break
            for j in range(hy):
                b = y ** j
                c = a + b
                if c > bound:
                    break
                result.add(c)
        return list(result)
       
