# https://leetcode.com/problems/valid-sudoku/
import collections
from typing import List


class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     rows_total = len(board)
    #     cols_total = len(board[0])
    #
    #     r_start, c_start = 0, 0
    #     r_end, c_end = r_start + 3, c_start + 3
    #
    #     rows_arr, cols_arr = [0] * rows_total, [0] * cols_total
    #     has_value = False
    #
    #     while r_start < rows_total and c_start < cols_total:
    #         visited = set()
    #         for r in range(r_start, r_end):
    #             for c in range(c_start, c_end):
    #                 value = board[r][c]
    #                 if value != '.':
    #                     if value in visited:
    #                         return False
    #                     visited.add(value)
    #                     rows_arr[r] = 1
    #                     cols_arr[c] = 1
    #
    #         r_start, c_start = r_end, c_end
    #         r_end, c_end = r_start + 3, c_start + 3
    #         if not has_value and visited:
    #             has_value = True
    #         visited.clear()
    #
    #     if not has_value:
    #         return True
    #
    #     for value in rows_arr:
    #         if not value:
    #             return False
    #
    #     for value in cols_arr:
    #         if not value:
    #             return False
    #
    #     return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                        board[r][c] in rows[r]
                        or board[r][c] in cols[c]
                        or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


if __name__ == '__main__':
    solution = Solution()

    # Input: board =
    # [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    #     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # Output: true
    print(solution.isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

    # Input: board =
    # [["8", "3", ".", ".", "7", ".", ".", ".", "."]
    #     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    #     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    #     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    #     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    #     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    #     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    #     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    #     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    # Output: false
    print(solution.isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

    # board =
    # [[".", ".", "4", ".", ".", ".", "6", "3", "."],
    #  [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #  ["5", ".", ".", ".", ".", ".", ".", "9", "."],
    #  [".", ".", ".", "5", "6", ".", ".", ".", "."],
    #  ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
    #  [".", ".", ".", "7", ".", ".", ".", ".", "."],
    #  [".", ".", ".", "5", ".", ".", ".", ".", "."],
    #  [".", ".", ".", ".", ".", ".", ".", ".", "."],
    #  [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    # Output: false
    print(solution.isValidSudoku(
        [[".", ".", "4", ".", ".", ".", "6", "3", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", "5", "6", ".", ".", ".", "."],
         ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
         [".", ".", ".", "7", ".", ".", ".", ".", "."],
         [".", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]))

    print(solution.isValidSudoku(
        [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]))

    print(solution.isValidSudoku(
        [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
         ["2", ".", ".", ".", ".", ".", ".", ".", "."],
         ["3", ".", ".", ".", ".", ".", ".", ".", "."],
         ["4", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", ".", "."],
         ["6", ".", ".", ".", ".", ".", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."],
         ["8", ".", ".", ".", ".", ".", ".", ".", "."],
         ["9", ".", ".", ".", ".", ".", ".", ".", "."]]))