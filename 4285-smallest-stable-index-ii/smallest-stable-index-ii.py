class Solution(object):
    def firstStableIndex(self, nums, k):
        n= len(nums)
        prefix_max = [0]*n
        prefix_max[0] = nums[0]
        for i in range(1,n):
            prefix_max[i] = max(prefix_max[i-1],nums[i])

        suff_min = [0]*n
        suff_min[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            suff_min[i] = min(suff_min[i+1],nums[i])
        
        for j in range(n):
            score = prefix_max[j] - suff_min[j]
            if score <= k:
                return j
        
        return -1

        