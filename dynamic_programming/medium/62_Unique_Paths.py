# https://leetcode.com/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * n
        for row in range(m - 1, -1, -1):
            curr_row = [0] * n
            curr_row[n - 1] = 1
            for col in range(n - 2, -1, -1):
                curr_row[col] = curr_row[col + 1] + prev_row[col]
            prev_row = curr_row
        return prev_row[0]


if __name__ == '__main__':
    solution = Solution()

    # Input: m = 3, n = 7
    # Output: 28
    print(solution.uniquePaths(3, 7))

    # Input: m = 3, n = 2
    # Output: 3
    print(solution.uniquePaths(3, 2))
