class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(n - k, n - 1)
        reverse(0, n - k - 1)
        reverse(0, n - 1)   
        