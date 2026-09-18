class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        mini = float("inf")
        low= 0
        high = n-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid] <= nums[high]:
                mini=min(mini,nums[mid])
                high = mid-1
            else:
                mini=min(mini,nums[low])
                low = mid+1
        return mini 

        
        