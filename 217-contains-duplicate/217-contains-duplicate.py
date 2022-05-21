class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        vals = {}
        for i in nums:
            if i in vals:
                return True
            else:
                vals[i] = None
                
        return False