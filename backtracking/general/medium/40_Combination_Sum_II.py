# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        total_len = len(candidates)

        def dfs(i, arr, curr_target: int):
            if curr_target == target:
                res.append(arr.copy())
                return
            elif curr_target > target or i >= total_len:
                return

            curr_target += candidates[i]
            arr.append(candidates[i])
            dfs(i + 1, arr, curr_target)

            curr_target -= candidates[i]
            arr.pop()
            dfs(i + 1, arr, curr_target)

        dfs(0, [], 0)
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: candidates = [10, 1, 2, 7, 6, 1, 5], target = 8
    # Output:
    # [
    #     [1, 1, 6],
    #     [1, 2, 5],
    #     [1, 7],
    #     [2, 6]
    # ]
    print(solution.combinationSum([10, 1, 2, 7, 6, 1, 5], 8))

    # Input: candidates = [2, 5, 2, 1, 2], target = 5
    # Output:
    # [
    #     [1, 2, 2],
    #     [5]
    # ]
    print(solution.combinationSum([2, 5, 2, 1, 2], 5))

