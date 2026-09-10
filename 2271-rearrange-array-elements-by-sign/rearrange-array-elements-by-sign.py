class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [0] * n
        pos_idx,neg_idx=0,1

        for i in range(0,n):
            if nums[i] >= 0:
                res[pos_idx] = nums [i]
                pos_idx +=2
            else:
                res[neg_idx] = nums[i]
                neg_idx +=2

        return res        
