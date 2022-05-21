class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_arr = [1] + [None] * len(nums) + [1]
        for i in range(len(nums)):
            pre_arr[i + 1] = nums[i] * pre_arr[i]
        
        post_arr = [1] + [None] * len(nums) + [1]
        for i in range(len(nums) - 1, -1, -1):
            post_arr[i + 1] = nums[i] * post_arr[i + 2]
        
        res = [None] * len(nums)
        for i in range(len(nums)):
            res[i] = pre_arr[i] * post_arr[i + 2]
        
        return res