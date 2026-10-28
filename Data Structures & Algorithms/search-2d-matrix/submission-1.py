class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1

        while l <= r:
            row = (l+r) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:
                l = 0
                r = len(matrix[row])-1

                while l <= r:
                    col = (l+r) // 2
                    if matrix[row][col] < target:
                        l = col+1
                    elif matrix[row][col] > target:
                        r = col-1
                    else:
                        return True

            elif matrix[row][-1] < target:
                l = row+1
            elif matrix[row][0] > target:
                r = row-1
            
        return False