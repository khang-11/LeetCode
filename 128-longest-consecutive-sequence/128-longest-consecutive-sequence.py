class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        
        res = 0
        for i in set_nums:
            if i - 1 not in set_nums:
                length = 1
                while i + 1 in set_nums:
                    length += 1
                    i += 1
                res = max(res, length)
                    
        return res
