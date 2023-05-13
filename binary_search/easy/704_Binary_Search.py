# https://leetcode.com/problems/binary-search/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
    # Output: 4
    print(solution.search([-1, 0, 3, 5, 9, 12], 9))

    # Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
    # Output: -1
    print(solution.search([-1, 0, 3, 5, 9, 12], 2))
