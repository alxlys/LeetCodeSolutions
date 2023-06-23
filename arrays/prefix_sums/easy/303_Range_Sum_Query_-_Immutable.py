# https://leetcode.com/problems/range-sum-query-immutable/
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            nums[i] = curr_sum
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sum_right = self.nums[right]
        sum_left = self.nums[left - 1] if left - 1 >= 0 else 0
        return sum_right - sum_left


if __name__ == '__main__':
    # Input
    # ["NumArray", "sumRange", "sumRange", "sumRange"]
    # [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
    # Output
    # [null, 1, -1, -3]
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    print(num_array.sumRange(0, 2))
    print(num_array.sumRange(2, 5))
    print(num_array.sumRange(0, 5))
