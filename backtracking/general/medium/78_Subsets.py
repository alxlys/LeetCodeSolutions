# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: nums = [1, 2, 3]
    # Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    print(solution.subsets([1, 2, 3]))

    # Input: nums = [0]
    # Output: [[], [0]]
    print(solution.subsets([0]))
