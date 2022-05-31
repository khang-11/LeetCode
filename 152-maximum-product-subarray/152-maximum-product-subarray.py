class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin, curMax = 1, 1
        res = float('-inf')
        
        for n in nums:
            i = curMin * n
            j = curMax * n
            curMax = max(i, j, n)
            curMin = min(i, j, n)
            res = max(res, curMax)
            
        return res