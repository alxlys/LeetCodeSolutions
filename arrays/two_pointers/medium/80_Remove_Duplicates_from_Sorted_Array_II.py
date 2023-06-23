# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        count = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
                count = 0
            elif nums[r] == nums[l] and count < 1:
                l += 1
                count += 1
                nums[l] = nums[r]

        return l + 1


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 1, 1, 2, 2, 3]
    # Output: 5, nums = [1, 1, 2, 2, 3, _]
    print(solution.removeDuplicates([1, 1, 1, 2, 2, 3]))

    # Input: nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    # Output: 7, nums = [0, 0, 1, 1, 2, 3, 3, _, _]
    print(solution.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
