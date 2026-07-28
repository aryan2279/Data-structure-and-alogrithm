class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #step1 : build frequency list:
        freq = [0]*26
        aId = ord('a')
        for c in s:
            freq[ord(c)-aId] += 1

        p1, p2 = [], []
        odd = -1
        for i, f in enumerate(freq):
            if f > 0:
                p1+= [chr(i+aId)]*(f//2)
                p2 = [chr(i+aId)]*(f//2) + p2
                if f%2 == 1:
                    odd = i
        if odd >= 0:
            p1.append(chr(odd+aId))
        return "".join(p1+p2)