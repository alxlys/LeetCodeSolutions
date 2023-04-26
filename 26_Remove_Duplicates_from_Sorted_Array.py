# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        return i + 1


if __name__ == '__main__':
    solution = Solution()

    nums = [1, 1, 2]
    print(nums)
    print(solution.removeDuplicates(nums))
    # Output: 2, nums = [1, 2, _]
    print(nums)

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(nums)
    print(solution.removeDuplicates(nums))
    # Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    print(nums)
