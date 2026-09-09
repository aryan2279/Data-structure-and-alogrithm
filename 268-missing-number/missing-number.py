class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        freq = {}
        for i in range (0,n+1):
            freq [i] = 0
        for num in nums:
            freq[num] =1
        for k , u in freq.items():
            if u==0:
                return k         
        