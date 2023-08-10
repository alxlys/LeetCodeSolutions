# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target_sum = nums[i] + nums[l] + nums[r]
                if target_sum > 0:
                    r -= 1
                elif target_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
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
