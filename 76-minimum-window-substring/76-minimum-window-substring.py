class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        search = {}
        for c in t:
            search[c] = search.get(c, 0) + 1
        unique = len(search)
        
        current = {}
        matches = 0
        res, shortest = None, float('inf')
        
        for r in range(len(s)):
            if s[r] in search:
                current[s[r]] = current.get(s[r], 0) + 1
                if current[s[r]] == search[s[r]]:
                    matches += 1
                    
                while matches == unique:
                    if r - l + 1 < shortest:
                        shortest = r - l + 1
                        res = l
                    
                    if s[l] in current:
                        current[s[l]] -= 1
                        if current[s[l]] == search[s[l]] - 1:
                            matches -= 1
                    l += 1
                              
        if shortest != float('inf'):
            return s[res: res + shortest]
        else:
            return ""