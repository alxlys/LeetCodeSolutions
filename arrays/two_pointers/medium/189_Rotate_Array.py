# https://leetcode.com/problems/rotate-array/
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        if k == 0:
            return

        def swap(l, r):
            while l < r:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                l += 1
                r -= 1

        l, r = 0, len(nums) - 1
        swap(l, r)

        l, r = 0, k - 1
        swap(l, r)

        l, r = k, len(nums) - 1
        swap(l, r)


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    # Output: [5, 6, 7, 1, 2, 3, 4]
    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 3)
    print(nums)

    # Input: nums = [-1, -100, 3, 99], k = 2
    # Output: [3, 99, -1, -100]
    nums = [-1, -100, 3, 99]
    solution.rotate(nums, 2)
    print(nums)
