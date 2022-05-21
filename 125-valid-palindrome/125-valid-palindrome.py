class Solution:
    def isPalindrome(self, s: str) -> bool:
        converted_string = ""
        for c in s:
            if c.isalpha() or c.isnumeric():
                converted_string += c.lower()
                
        for i in range(len(converted_string) // 2):
            if converted_string[i] != converted_string[- i - 1]:
                return False
            
        return True