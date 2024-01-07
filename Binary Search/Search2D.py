class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) * len(matrix[0]) - 1
        while start <= end:
            mid = start + int((end - start) / 2)
            if matrix[int(mid / len(matrix[0]))][int(mid % len(matrix[0]))] == target:
                return True
            elif matrix[int(mid / len(matrix[0]))][int(mid % len(matrix[0]))] < target:
                start = mid + 1
            else:
                end = mid - 1
        return False
