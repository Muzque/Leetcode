"""
9 / 9 test cases passed.
Status: Accepted
Runtime: 652 ms
Memory Usage: 37.4 MB
"""
class WordFilter:
    def _posibility(self, word, idx):
        h = len(word)
        for i in range(h):
            prefix = word[:i+1]
            for j in range(h):
                suffix = word[h-j-1:]
                self.cache[f'{prefix}#{suffix}'] = idx

    def __init__(self, words: List[str]):
        self.cache = {}
        for idx, word in enumerate(words):
            self._posibility(word, idx)
    
    def f(self, prefix: str, suffix: str) -> int: 
        return self.cache.get(f'{prefix}#{suffix}', -1)
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
