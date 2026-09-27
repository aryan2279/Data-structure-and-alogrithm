class Solution(object):
    def minBitFlips(self, start, goal):
        temp = start ^ goal
        count = 0
        while temp > 0:
            if temp % 2 != 0:
                count += 1
            temp = temp // 2     
        return count