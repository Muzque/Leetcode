class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xb = bin(x)[2:]
        yb = bin(y)[2:]
        if len(xb) < len(yb):
            xb = xb.zfill(len(yb))
        else:
            yb = yb.zfill(len(xb))
        count = 0
        for i in range(len(xb)):
            if xb[i] != yb[i]:
                count = count +1
        return count