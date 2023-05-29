# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_map = {}
        i = 0
        for num in nums:
            if target - num not in sum_map:
                sum_map[num] = i
                i += 1
            else:
                return [sum_map[target - num], i]


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [2, 7, 11, 15], target = 9
    # Output: [0, 1]
    print(solution.twoSum([2, 7, 11, 15], 9))

    # Input: nums = [3, 2, 4], target = 6
    # Output: [1, 2]
    print(solution.twoSum([3, 2, 4], 6))

    # Input: nums = [3, 3], target = 6
    # Output: [0, 1]
    print(solution.twoSum([3, 3], 6))
