from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target < matrix[i][-1]:
                if target in matrix[i]:
                    return True
        return False
    
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:     
                lo = 0
                hi = len(matrix[0])
                while lo <= hi:
                    mid = lo + (hi - lo) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] > target:
                        hi = mid - 1 
                    else:
                        lo = mid + 1
        return False            
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        lo = 0
        hi = len(matrix) * len(matrix[0])
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            i = mid // len(matrix)
            j = mid %len(matrix)
            
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                hi = j - 1 
            else:
                lo = j + 1
        return False 

a = Solution()
print(a.searchMatrix([[1]], 1))