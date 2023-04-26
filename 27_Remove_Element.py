# https://leetcode.com/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        end = len(nums) - 1
        i = 0
        while i <= end:
            if nums[i] == val:
                temp = nums[end]
                nums[end] = nums[i]
                nums[i] = temp
                end -= 1
            else:
                i += 1
        return i


if __name__ == '__main__':
    solution = Solution()

    nums = [3, 2, 2, 3]
    val = 3
    print(solution.removeElement(nums, val))
    # Output: 2, nums = [2, 2, _, _]
    print(nums)

    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print(solution.removeElement(nums, val))
    # Output: 5, nums = [0,1,4,0,3,_,_,_]
    print(nums)
