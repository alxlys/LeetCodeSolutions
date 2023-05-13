# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        arr = None
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][len(matrix[mid]) - 1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                arr = matrix[mid]
                break

        if not arr:
            return False

        l, r = 0, len(arr) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > arr[mid]:
                l = mid + 1
            elif target < arr[mid]:
                r = mid - 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()

    # Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 3
    # Output: true
    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))

    # Input: matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target = 13
    # Output: false
    print(solution.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
