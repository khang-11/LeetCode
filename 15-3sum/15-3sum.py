class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        
        for i in range(len(nums) - 2):
            if i > 0 and sorted_nums[i - 1] == sorted_nums[i]:
                continue
            target = -sorted_nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                sm = sorted_nums[l] + sorted_nums[r]

                if sm > target:
                    r -= 1

                elif sm < target:
                    l += 1

                else:
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    while l < r and sorted_nums[l] == sorted_nums[l + 1]:
                        l += 1
                    while l < r and sorted_nums[r] == sorted_nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res
                        
            