# https://leetcode.com/problems/word-search/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return False

        path = set()

        def dfs(m: int, n: int, i: int) -> bool:
            # out of letter in a word -> success
            if i == len(word):
                return True
            if m == len(board) or n == len(board[m]) or m < 0 or n < 0:
                # out of bounds
                return False
            if word[i] != board[m][n]:
                # letter doesn't match, not need to continue
                return False
            if (m, n) in path:
                # this path is already passed
                return False
            path.add((m, n))

            res = dfs(m + 1, n, i + 1) or dfs(m, n + 1, i + 1) or dfs(m - 1, n, i + 1) or dfs(m, n - 1, i + 1)
            path.remove((m, n))
            return res

        for m in range(len(board)):
            for n in range(len(board[m])):
                if word[0] == board[m][n]:
                    if dfs(m, n, 0):
                        return True

        return False


if __name__ == '__main__':
    solution = Solution()

    # Input: board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word = "ABCCED"
    # Output: true
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))

    # Input: board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word = "SEE"
    # Output: true
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))

    # Input: board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word = "ABCB"
    # Output: false
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
