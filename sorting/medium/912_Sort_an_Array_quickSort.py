# https://leetcode.com/problems/sort-an-array/
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.__quick_sort__(nums, 0, len(nums) - 1)
        return nums

    def __quick_sort__(self, nums: List[int], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return

        pivot = nums[e]
        left = s

        for i in range(s, e):
            if nums[i] < pivot:
                tmp = nums[i]
                nums[i] = nums[left]
                nums[left] = tmp
                left += 1

        nums[e] = nums[left]
        nums[left] = pivot

        self.__quick_sort__(nums, s, left - 1)
        self.__quick_sort__(nums, left + 1, e)


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [5, 2, 3, 1]
    # Output: [1, 2, 3, 5]
    print(solution.sortArray([5, 2, 3, 1]))

    # Input: nums = [5, 1, 1, 2, 0, 0]
    # Output: [0, 0, 1, 1, 2, 5]
    print(solution.sortArray([5, 1, 1, 2, 0, 0]))
