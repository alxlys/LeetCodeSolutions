# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_sub_arr_len = len(nums) + 1  # cannot be larger than this
        sum_sub_arr = 0

        for right in range(len(nums)):
            sum_sub_arr += nums[right]
            while sum_sub_arr >= target:
                min_sub_arr_len = min(min_sub_arr_len, right - left + 1)
                sum_sub_arr -= nums[left]
                left += 1
        return min_sub_arr_len if min_sub_arr_len < len(nums) + 1 else 0


if __name__ == '__main__':
    solution = Solution()

    # Input: target = 7, nums = [2, 3, 1, 2, 4, 3]
    # Output: 2
    print(solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))

    # Input: target = 4, nums = [1, 4, 4]
    # Output: 1
    print(solution.minSubArrayLen(4, [1, 4, 4]))

    # Input: target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
    # Output: 0
    print(solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
