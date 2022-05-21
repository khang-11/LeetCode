class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_occ, s2_occ = [0] * 26, [0] * 26
        matches = 0
        
        for i in range(len(s1)):
            s1_occ[ord(s1[i]) - ord('a')] += 1
            s2_occ[ord(s2[i]) - ord('a')] += 1
            
        for i in range(26):
            matches += 1 if s1_occ[i] == s2_occ[i] else 0
                  
        if matches == 26:
            return True
            
        for i in range(len(s1), len(s2)):    
       
            r_index = ord(s2[i]) - ord('a')
            l_index = ord(s2[i - len(s1)]) - ord('a')
            
            s2_occ[r_index] += 1
            if s2_occ[r_index] == s1_occ[r_index]:
                matches += 1
            elif s2_occ[r_index] - 1 == s1_occ[r_index]:
                matches -= 1
               
            s2_occ[l_index] -= 1
            if s2_occ[l_index] == s1_occ[l_index]:
                matches += 1
            elif s2_occ[l_index] + 1 == s1_occ[l_index]:
                matches -= 1
                
            if matches == 26:
                return True

        return False