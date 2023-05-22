# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i, sum_total):
            if sum_total == target:
                res.append(subset.copy())
                return
            if i >= len(candidates) or sum_total > target:
                return
            subset.append(candidates[i])
            dfs(i, sum_total + candidates[i])
            # decision NOT to include number
            subset.pop()
            dfs(i + 1, sum_total)

        dfs(0, 0)
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: candidates = [2, 3, 6, 7], target = 7
    # Output: [[2, 2, 3], [7]]
    print(solution.combinationSum([2, 3, 6, 7], 7))

    # Input: candidates = [2, 3, 5], target = 8
    # Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    print(solution.combinationSum([2, 3, 5], 8))

    # Input: candidates = [2], target = 1
    # Output: []
    print(solution.combinationSum([2], 1))
