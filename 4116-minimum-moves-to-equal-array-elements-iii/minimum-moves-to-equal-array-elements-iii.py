class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        ans = 0
        for num in nums:
            ans += (mx - num)

        return ans