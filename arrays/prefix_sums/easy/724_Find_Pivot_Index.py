# https://leetcode.com/problems/find-pivot-index/
from typing import List


class Solution:

    # my clumsy solution
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum_arr = [0] * len(nums)
        right_sum_arr = [0] * len(nums)
        left_sum, right_sum, l, r = 0, 0, 0, len(nums) - 1
        while l < len(nums) and r >= 0:
            left_sum_arr[l] = left_sum
            left_sum += nums[l]
            l += 1
            right_sum_arr[r] = right_sum
            right_sum += nums[r]
            r -= 1
        for i in range(len(nums)):
            if left_sum_arr[i] == right_sum_arr[i]:
                return i
        return -1

    # elegant neetcode solution
    def pivot_index(self, nums: List[int]) -> int:
        total = sum(nums)  # O(n)

        leftSum = 0
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
        return -1


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 7, 3, 6, 5, 6]
    # Output: 3
    print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))

    # Input: nums = [1, 2, 3]
    # Output: -1
    print(solution.pivotIndex([1, 2, 3]))

    # Input: nums = [2, 1, -1]
    # Output: 0
    print(solution.pivotIndex([2, 1, -1]))
