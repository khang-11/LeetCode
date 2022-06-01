class Solution:
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        
        def search(vals, target, path):
            if target == 0:
                self.res.append(path)
            else:
                for i in range(len(vals)):
                    if vals[i] <= target:
                        search(vals[i:], target - vals[i], path + [vals[i]])
        
        search(candidates, target, [])
        return self.res
            
        