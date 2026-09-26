class Solution:
    def containsNearbyDuplicate(self, nums, k):
        s = set()

        for i, num in enumerate(nums):
            if num in s:
                return True

            s.add(num)

            if len(s) > k:
                s.remove(nums[i - k])

        return False