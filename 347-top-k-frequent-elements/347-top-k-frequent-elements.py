import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_occ = {}
        h = []
        
        for n in nums:
            if n not in nums_occ:
                nums_occ[n] = 1
            else:
                nums_occ[n] += 1
                
        buckets = [None] * (len(nums) + 1)
        for n in nums_occ:
            if buckets[nums_occ[n]] == None:
                buckets[nums_occ[n]] = [n]
            else:
                buckets[nums_occ[n]].append(n)
            
        res = []
        for i in buckets:
            if i:
                res += i
            
        return res[len(res) - k:len(res)]