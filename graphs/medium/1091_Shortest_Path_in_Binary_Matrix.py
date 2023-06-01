# https://leetcode.com/problems/shortest-path-in-binary-matrix/
from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque()
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def bfs() -> int:
            path_length = 0
            while queue:
                for i in range(len(queue)):
                    r, c = queue.popleft()
                    if r == rows - 1 and c == cols - 1:
                        return path_length + 1
                    neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
                    for dr, dc in neighbors:
                        if min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols or (r + dr, c + dc) in visited or \
                                grid[r + dr][c + dc] == 1:
                            continue
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
                path_length += 1
            return -1

        queue.append((0, 0))
        visited.add((0, 0))
        return bfs()


if __name__ == '__main__':
    solution = Solution()

    # Input:
    grid = [[0, 1], [1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))
    # Output: 2

    # Input:
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))
    # Output: 4

    # Input:
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    print(solution.shortestPathBinaryMatrix(grid))
    # Output: -1
