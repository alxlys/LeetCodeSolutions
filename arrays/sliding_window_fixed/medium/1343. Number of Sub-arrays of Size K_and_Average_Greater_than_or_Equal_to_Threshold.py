# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sub_arr_sum = 0
        left = 0
        res = 0
        for right in range(len(arr)):
            if right - left + 1 > k:
                sub_arr_sum -= arr[left]
                left += 1
            sub_arr_sum += arr[right]
            if right - left + 1 == k and sub_arr_sum // k >= threshold:
                res += 1
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4
    # Output: 3
    print(solution.numOfSubarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))

    # Input: arr = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3], k = 3, threshold = 5
    # Output: 6
    print(solution.numOfSubarrays([11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5))
