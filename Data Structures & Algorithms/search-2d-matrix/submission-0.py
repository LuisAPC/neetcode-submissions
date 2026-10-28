class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:

            if row[0] <= target <= row[-1]:
                l = 0
                r = len(row)-1

                while l <= r:
                    m = (l+r) // 2
                    if row[m] < target:
                        l = m+1
                    elif row[m] > target:
                        r = m-1
                    else:
                        return True
            
        return False