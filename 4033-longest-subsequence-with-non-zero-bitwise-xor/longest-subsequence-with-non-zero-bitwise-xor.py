class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)
        xor = 0
        countZero = 0

        for num in nums:
            if num == 0:
                countZero += 1
            xor ^= num

        if xor != 0:
            return n
        if countZero == n:
            return 0

        return n - 1