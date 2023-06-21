# https://leetcode.com/problems/longest-turbulent-subarray/
import math
from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left, right = 0, 1
        res = 1
        prev = ''
        while right < len(arr):
            if arr[right - 1] < arr[right] and prev != '<':
                res = max(res, right - left + 1)
                right += 1
                prev = '<'
            elif arr[right - 1] > arr[right] and prev != '>':
                res = max(res, right - left + 1)
                right += 1
                prev = '>'
            else:
                right = right + 1 if arr[right - 1] == arr[right] else right
                left = right - 1
                prev = ''
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    # Output: 5
    # Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
    print(solution.maxTurbulenceSize([9, 4, 2, 10, 7, 8, 8, 1, 9]))

    # Input: arr = [4, 8, 12, 16]
    # Output: 2
    print(solution.maxTurbulenceSize([4, 8, 12, 16]))

    # Input: arr = [100]
    # Output: 1
    print(solution.maxTurbulenceSize([100]))
