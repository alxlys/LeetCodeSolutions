# https://leetcode.com/problems/search-in-rotated-sorted-array/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if nums[m] == target:
                return m
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return -1


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
    # Output: 4
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))

    # Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
    # Output: -1
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))

    # Input: nums = [1], target = 0
    # Output: -1
    print(solution.search([1], 0))
