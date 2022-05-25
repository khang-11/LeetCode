class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            dp.append([None] * n)
        dp[0][0] = 1
        
        def helper(i, j):
            if i not in range(m):
                return 0
            if j not in range(n):
                return 0
            if dp[i][j] != None:
                return dp[i][j]
            else:
                dp[i][j] = helper(i - 1, j) + helper(i, j - 1)
                return dp[i][j]
            
        return helper(m - 1, n - 1)