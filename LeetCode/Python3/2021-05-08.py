"""

"""
"""
TLE
"""
import math

class Solution:
    def is_palindrome(self, n):
        if n < 10: return True
        word = str(n)
        mid = len(word) // 2
        return word[:mid] == word[:len(word)-mid-1:-1]
        
    
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = math.ceil(int(left) ** 0.5)
        right = math.ceil(int(right) ** 0.5)
        cnt = 0
        for num in range(left, right):
            if self.is_palindrome(num):
                if self.is_palindrome(num**2):
                    cnt += 1
        return cnt
