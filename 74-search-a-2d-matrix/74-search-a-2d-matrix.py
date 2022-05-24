class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i, j = 0, len(matrix) * len(matrix[0]) - 1
        while i < j:
            m = i + (j - i) // 2
            if target > matrix[m // len(matrix[0])][m % len(matrix[0])]:
                i = m + 1
            else:
                j = m
                
        return matrix[i // len(matrix[0])][i % len(matrix[0])] == target