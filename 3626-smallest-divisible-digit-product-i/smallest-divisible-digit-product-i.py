class Solution(object):
    def smallestNumber(self, n, t):

        def product(n):
            pro = 1
            while n > 0:
                pro *= n % 10
                n /= 10
            return pro

        while product(n) % t != 0:
            n += 1

        return n