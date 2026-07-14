class Solution:
    mod = 10**9 + 7

    def subsequencePairCount(self, nums: List[int]) -> int:
        n = len(nums)
        maxEl = max(nums)

        dp = [[[-1] * (maxEl + 1) for _ in range(maxEl + 1)] for _ in range(n)]

        def f(i, g1, g2):
            # Base Case:
            # All elements have been processed.
            # Count only if both subsequences are non-empty
            # and their GCDs are equal.
            if i == -1:
                if g1 != 0 and g2 != 0 and g1 == g2:
                    return 1
                return 0

            # Return memoized result.
            if dp[i][g1][g2] != -1:
                return dp[i][g1][g2]

            # Option 1: Ignore current element.
            notTake = f(i - 1, g1, g2)

            # Option 2: Put current element into first subsequence.
            g1Take = f(i - 1, math.gcd(g1, nums[i]), g2)

            # Option 3: Put current element into second subsequence.
            g2Take = f(i - 1, g1, math.gcd(g2, nums[i]))

            dp[i][g1][g2] = (notTake + g1Take + g2Take) % self.mod
            return dp[i][g1][g2]

        return f(n - 1, 0, 0)