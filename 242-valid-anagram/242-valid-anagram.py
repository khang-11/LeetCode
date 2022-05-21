class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        characters = {}
        for c in s:
            if c in characters:
                characters[c] += 1
            else:
                characters[c] = 1
                
        for c in t:
            if c not in characters:
                return False
            elif c in characters:
                if characters[c] == 1:
                    del characters[c]
                else:
                    characters[c] -= 1
                    
        if len(characters) == 0:
            return True
        else:
            return False