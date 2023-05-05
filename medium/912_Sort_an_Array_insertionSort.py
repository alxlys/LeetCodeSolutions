# https://leetcode.com/problems/sort-an-array/
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0 and nums[j + 1] < nums[j]:
                temp = nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = temp
                j -= 1
        return nums


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [5, 2, 3, 1]
    # Output: [1, 2, 3, 5]
    print(solution.sortArray([5, 2, 3, 1]))

    # Input: nums = [5, 1, 1, 2, 0, 0]
    # Output: [0, 0, 1, 1, 2, 5]
    print(solution.sortArray([5, 1, 1, 2, 0, 0]))
