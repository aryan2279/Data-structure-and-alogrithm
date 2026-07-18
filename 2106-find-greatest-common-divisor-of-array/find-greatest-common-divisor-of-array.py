class Solution(object):
    def findGCD(self, nums):
        mi=min(nums)
        ma=max(nums)
        a=[]
        for i in range(1,mi+1):
            if mi%i==0 and ma%i==0:
                a.append(i)
        return max(a)


        