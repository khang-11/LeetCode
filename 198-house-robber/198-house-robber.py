class Solution:
    def rob(self, nums: List[int]) -> int:   
        dp = [None] * len(nums)
        dp[0] = nums[0]
        res = nums[0]
    
        for i in range(1, len(nums)):
            if i == 1:
                dp[i] = max(nums[1], dp[0])
            else:
                dp[i] = max(dp[i-1], nums[i] + dp[i-2])
                
            res = max(res, dp[i])
            
        return res