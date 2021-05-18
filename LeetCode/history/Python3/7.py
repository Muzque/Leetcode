class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 0:
            x = str(x)
            rev = int(x[::-1])
        else:
            x = str(abs(x))
            rev = int('-'+x[::-1])
        if (rev >= 2**31) or (rev < -2**31):
            return 0
        else:
            return rev