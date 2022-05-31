class Solution:
    def countSubstrings(self, s: str) -> int:
        def find_longest_odd_palindrome(i):
            length = 1
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                l -= 1
                r += 1
            return length
        
        def find_longest_even_palindrome(i):
            length = 0
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                l -= 1
                r += 1
            return length
        
        res = 0
        for i in range(len(s)):
            res += int(find_longest_odd_palindrome(i) // 2) + 1
            res += int(find_longest_even_palindrome(i) / 2)
            
        return res