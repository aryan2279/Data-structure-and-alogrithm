class Solution(object):
    def gcdValues(self, nums, queries):
        mx = max(nums)
        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)
        for g in range(1, mx + 1):
            s = 0
            for multiple in range(g, mx + 1, g):
                s += freq[multiple]
            cnt[g] = s

        exact = [0] * (mx + 1)
        for g in range(mx, 0, -1):
            c = cnt[g]
            pairs = c * (c - 1) // 2
            multiple = 2 * g
            while multiple <= mx:
                pairs -= exact[multiple]
                multiple += g
            exact[g] = pairs

        prefix = [0] * (mx + 1)
        for g in range(1, mx + 1):
            prefix[g] = prefix[g - 1] + exact[g]

        ans = []

        for q in queries:
            target = q + 1  
            lo, hi = 1, mx
            while lo < hi:
                mid = (lo + hi) // 2
                if prefix[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            ans.append(lo)

        return ans