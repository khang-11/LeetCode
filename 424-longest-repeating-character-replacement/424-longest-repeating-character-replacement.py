class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freq = {}
        max_f = 0
        
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_f = max(max_f, freq[s[r]])
                
            while (r - l + 1) - max_f > k:
                freq[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
            
        return res
                