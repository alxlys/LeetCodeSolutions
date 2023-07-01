# https://leetcode.com/problems/subsets-ii/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
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
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.__helper__(i + 1, nums, curr_set, subsets)


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 2, 2]
    # Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
    print(solution.subsetsWithDup([1, 2, 2]))

    # Input: nums = [0]
    # Output: [[], [0]]
    print(solution.subsetsWithDup([0]))
