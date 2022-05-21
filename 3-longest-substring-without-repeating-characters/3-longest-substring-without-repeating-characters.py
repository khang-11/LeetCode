class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = {}
        res = 0
        l, r = 0, 0
        
        for r in range(len(s)):
            if s[r] in c:
                l = max(l, c[s[r]] + 1)

            res = max(res, r - l + 1)
            c[s[r]] = r
     
        return res