# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    # TODO doesn't work
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        l, m, r = 0, 1, len(nums) - 1
        res = []
        while l < (r - 1):
            while m < r:
                if (nums[l] + nums[m] + nums[r]) == 0:
                    res.append([nums[l], nums[m], nums[r]])
                m += 1
            # l += 1
            m = l + 1
            r -= 1
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [-1, 0, 1, 2, -1, -4]
    # Output: [[-1, -1, 2], [-1, 0, 1]]
    print(solution.threeSum([-1, 0, 1, 2, -1, -4]))

    # Input: nums = [0, 1, 1]
    # Output: []
    print(solution.threeSum([0, 1, 1]))

    # Input: nums = [0, 0, 0]
    # Output: [[0, 0, 0]]
    print(solution.threeSum([0, 0, 0]))
