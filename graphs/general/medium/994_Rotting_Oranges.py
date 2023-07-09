# https://leetcode.com/problems/rotting-oranges/
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def bfs(queue: deque, fresh_oranges: int) -> int:
            path_length = 0
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                    for dr, dc in neighbors:
                        if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or grid[r + dr][c + dc] != 1:
                            continue
                        grid[r + dr][c + dc] = 2
                        fresh_oranges -= 1
                        queue.append((r + dr, c + dc))
                if queue:
                    path_length += 1
            return path_length if not fresh_oranges else -1

        # 2s can be in several parts of grid, so we might need to go from several sides simultaneously
        _queue = deque()
        _fresh_oranges = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    _queue.append((r, c))
                elif grid[r][c] == 1:
                    _fresh_oranges += 1

        return bfs(_queue, _fresh_oranges)


if __name__ == '__main__':
    solution = Solution()

    # Input:
    grid = [[2, 1, 1],
            [1, 1, 0],
            [0, 1, 1]]
    print(solution.orangesRotting(grid))
    # Output: 4

    # Input:
    grid = [[2, 1, 1],
            [0, 1, 1],
            [1, 0, 1]]
    print(solution.orangesRotting(grid))
    # Output: -1

    # Input:
    grid = [[0, 2]]
    print(solution.orangesRotting(grid))
    # Output: 0

    # Input:
    grid = [[1, 2]]
    print(solution.orangesRotting(grid))
    # Output: 1

    # Input:
    grid = [[2, 1, 1],
            [1, 1, 1],
            [0, 1, 2]]
    print(solution.orangesRotting(grid))
    # Output: 2
