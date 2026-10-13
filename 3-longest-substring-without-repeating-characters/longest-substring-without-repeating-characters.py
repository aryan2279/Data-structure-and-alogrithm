class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        left = 0
        maxi = 0
        n = len(s)

        for right in range(n):
            if s[right] in last_seen:
                left = max(left, last_seen[s[right]] + 1)
            last_seen[s[right]] = right
            maxi = max(maxi, right - left + 1)

        return maxi