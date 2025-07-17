class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rightArr = len(matrix) - 1
        leftArr = 0

        while leftArr <= rightArr:
            midArr = (rightArr + leftArr) // 2

            right = len(matrix[midArr]) - 1
            left = 0

            while left <= right:
                mid = (right + left) // 2

                if matrix[midArr][mid] > target:
                    right = mid - 1
                    rightArr = midArr - 1
                
                elif matrix[midArr][mid] < target:
                    left = mid + 1
                    leftArr = midArr + 1
                
                else: 
                    return True

        return False