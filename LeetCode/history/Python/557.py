class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        y = []
        for line in s:
            y.append(line[::-1])

        return ' '.join(y)