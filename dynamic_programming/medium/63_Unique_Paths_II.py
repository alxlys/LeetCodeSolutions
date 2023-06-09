# https://leetcode.com/problems/unique-paths-ii/
import math
from typing import List


class Solution:
    # My clumsy solution
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        row_length = len(obstacleGrid)
        col_length = len(obstacleGrid[0])
        if obstacleGrid[row_length - 1][col_length - 1] == 1:
            return 0
        prev_row = [0] * col_length
        prev_row[col_length - 1] = 1
        for row in range(row_length - 1, -1, -1):
            curr_row = obstacleGrid[row]
            if curr_row[col_length - 1] == 1:
                curr_row[col_length - 1] = 'D'
            elif prev_row[col_length - 1] == 0 or prev_row[col_length - 1] == 'D':
                curr_row[col_length - 1] = 0
            else:
                curr_row[col_length - 1] = 1

            for col in range(col_length - 2, -1, -1):
                if curr_row[col] == 1:
                    curr_row[col] = 'D'
                    continue

                curr_row_prev_value = curr_row[col + 1] if curr_row[col + 1] != 'D' else 0
                prev_row_prev_value = prev_row[col] if prev_row[col] != 'D' else 0

                curr_row[col] = curr_row_prev_value + prev_row_prev_value

            prev_row = curr_row

        return prev_row[0] if prev_row[0] != 'D' else 0

    # Elegant neetcode solution
    def unique_paths_with_obstacles(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dp = [0] * N
        dp[N - 1] = 1

        # Time: O(N*M), Space: O(N)
        for r in reversed(range(M)):
            for c in reversed(range(N)):
                if grid[r][c]:
                    dp[c] = 0
                elif c + 1 < N:
                    dp[c] = dp[c] + dp[c + 1]
        return dp[0]


if __name__ == '__main__':
    solution = Solution()

    # Input: obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    # Output: 2
    print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

    # Input: obstacleGrid = [[0, 1], [0, 0]]
    # Output: 1
    print(solution.uniquePathsWithObstacles([[0, 1], [0, 0]]))

    # Input: obstacleGrid = [[0,0],[0,1]]
    # Output: 0
    print(solution.uniquePathsWithObstacles([[0, 0], [0, 1]]))

    # [[0, 0]]
    print(solution.uniquePathsWithObstacles([[0, 0]]))

    # [[0, 1]]
    print(solution.uniquePathsWithObstacles([[0, 1]]))
