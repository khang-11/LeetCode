class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        sm = numbers[l] + numbers[r]
        
        while sm != target:
            
            
            if sm < target:
                l += 1
            else:
                r -= 1
                
            sm = numbers[l] + numbers[r]
                   
        return [l + 1, r + 1]