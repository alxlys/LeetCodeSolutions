# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        l = 0
        for r in range(1, len(nums)):
            if nums[l] == 0 and nums[r] != 0:
                nums[l] = nums[r]
                nums[r] = 0

            if nums[l] != 0:
                l += 1


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [0, 1, 0, 3, 12]
    # Output: [1, 3, 12, 0, 0]
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)

    # Input: nums = [0]
    # Output: [0]
    nums = [0]
    solution.moveZeroes(nums)
    print(nums)
