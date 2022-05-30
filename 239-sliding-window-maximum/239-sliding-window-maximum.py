from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        dq = deque()
        for i in range(k):
            while len(dq) != 0 and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        res.append(nums[dq[0]])
        
        for i in range(k, len(nums)):
            
            # pop out of bound indexes
            while len(dq) != 0 and dq[0] <= i - k:
                dq.popleft()
                
            # pop invalid smaller numbers
            while len(dq) != 0 and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            
            res.append(nums[dq[0]])
            
        return res