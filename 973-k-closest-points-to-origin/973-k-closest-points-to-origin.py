import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        
        for point in points:
            distance = point[0]**2 + point[1]**2
            heapq.heappush(h, (-distance, point))
            if len(h) > k:
                heapq.heappop(h)
            
        return [x[1] for x in h]