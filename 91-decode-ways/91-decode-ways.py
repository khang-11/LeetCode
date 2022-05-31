class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1
        
        dp = [None] * len(s)
        dp[0] = 1
        if int(s[1]) == 0:
            if int(s[0]) in range(1, 3):
                dp[1] = 1
            else:
                return 0
        elif int(s[1]) in range(1, 10) and s[0] == "1":
            dp[1] = 2
        elif int(s[1]) in range(1, 7) and s[0] == "2":
            dp[1] = 2
        else:
            dp[1] = 1
        
        for i in range(2, len(s)):
            if int(s[i]) == 0:
                if int(s[i-1]) in range(1, 3):
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif int(s[i]) in range(1, 10) and s[i-1] == "1":
                dp[i] = dp[i-1] + dp[i-2]
            elif int(s[i]) in range(1, 7) and s[i-1] == "2":
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
                
        return dp[len(s)-1]