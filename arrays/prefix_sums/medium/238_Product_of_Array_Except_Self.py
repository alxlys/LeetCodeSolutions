# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:

    # and my clumsy solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_pov_arr = [0] * len(nums)
        right_pov_arr = [0] * len(nums)
        left_pov, right_pov, l, r = 1, 1, 0, len(nums) - 1
        while l < len(nums) and r >= 0:
            left_pov *= nums[l]
            left_pov_arr[l] = left_pov
            l += 1
            right_pov *= nums[r]
            right_pov_arr[r] = right_pov
            r -= 1
        res = []
        for i in range(len(nums)):
            left = left_pov_arr[i - 1] if i - 1 >= 0 else 1
            right = right_pov_arr[i + 1] if i + 1 < len(nums) else 1
            res.append(left * right)
        return res

    # as always proper neetcode solution
    def product_except_self(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 2, 3, 4]
    # Output: [24, 12, 8, 6]
    print(solution.productExceptSelf([1, 2, 3, 4]))

    # Input: nums = [-1, 1, 0, -3, 3]
    # Output: [0, 0, 9, 0, 0]
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
