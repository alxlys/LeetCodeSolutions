# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        # Array is not rotated
        if nums[r] > nums[l]:
            return nums[l]
        res = nums[0]

        while l <= r:
            m = (r + l) // 2
            res = min(res, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [3, 4, 5, 1, 2]
    # Output: 1
    print(solution.findMin([3, 4, 5, 1, 2]))

    # Input: nums = [4, 5, 6, 7, 0, 1, 2]
    # Output: 0
    print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))

    # Input: nums = [6, 7, 0, 1, 2, 4, 5]
    # Output: 0
    print(solution.findMin([6, 7, 0, 1, 2, 4, 5]))

    # Input: nums = [11, 13, 15, 17]
    # Output: 11
    print(solution.findMin([11, 13, 15, 17]))
