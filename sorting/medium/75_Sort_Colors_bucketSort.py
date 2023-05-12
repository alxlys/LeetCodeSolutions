# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for n in nums:
            count[n] += 1

        i = 0
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i += 1


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [2, 0, 2, 1, 1, 0]
    # Output: [0, 0, 1, 1, 2, 2]
    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    print(nums)

    # Input: nums = [2,0,1]
    # Output: [0,1,2]
    nums = [2, 0, 1]
    print(solution.sortColors(nums))
    print(nums)
