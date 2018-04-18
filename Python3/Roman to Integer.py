class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numlist = []
        for x in s:
            if x == 'I':
                num = 1
            elif x == 'V':
                num = 5
            elif x == 'X':
                num = 10
            elif x == 'L':
                num = 50
            elif x == 'C':
                num = 100
            elif x == 'D':
                num = 500
            elif x == 'M':
                num = 1000
            numlist.append(num)
        total = 0
        temp = 0
        if len(numlist) == 1:
            return numlist[0]
        else:
            for j in range(1, len(numlist)):
                if numlist[j-1] >= numlist[j]:
                    total += numlist[j-1] - temp
                    temp = 0
                elif j == len(numlist)-1:
                    total += numlist[j] - numlist[j-1]
                else:
                    temp = numlist[j-1]
            if numlist[-2] >= numlist[-1]:
                total += numlist[-1]
            return total