class Solution(object):
    def gcdOfOddEvenSums(self, n):
        a=(n*(4+(n-1)*2))/2;
        b=(n*(2+(n-1)*2))/2;
        while(b):
            a,b=b,a%b
        return a
        """
        :type n: int
        :rtype: int
        """
        