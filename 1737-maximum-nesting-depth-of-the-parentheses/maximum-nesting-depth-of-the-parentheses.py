class Solution(object):
    def maxDepth(self, s):
        ans = depth = 0
        for ch in s:
            depth += (ch == "(") - (ch == ")")
            ans = max(ans, depth)
        return ans
        
        