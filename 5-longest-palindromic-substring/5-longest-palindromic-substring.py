class Solution:
    def longestPalindrome(self, s: str) -> str:
        
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
        
        res = ""
        longest = float('-inf')
        
        for i in range(len(s)):
            longest_even = find_longest_even_palindrome(i)
            if longest_even > longest:
                start = int(i - longest_even / 2 + 1)
                end = int(i + longest_even / 2 + 1)
                res = s[start:end]
                longest = longest_even
                
            longest_odd = find_longest_odd_palindrome(i)
            if longest_odd > longest:
                start = int(i - longest_odd // 2)
                end = int(i + longest_odd // 2 + 1)
                res = s[start:end]
                longest = longest_odd
                
        return res