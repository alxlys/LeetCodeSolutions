# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        curr_set, subsets = [], []
        self.__helper__(0, nums, curr_set, subsets)
        return subsets

    def __helper__(self, i, nums, curr_set, subsets):
        if i == len(nums):
            subsets.append(curr_set.copy())
            return
        curr_set.append(nums[i])
        self.__helper__(i + 1, nums, curr_set, subsets)
        curr_set.pop()
        self.__helper__(i + 1, nums, curr_set, subsets)


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 2, 3]
    # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(solution.subsets([1, 2, 3]))

    # Input: nums = [0]
    # Output: [[], [0]]
    print(solution.subsets([0]))
