# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = grid[i + 1][j + 1] + 1
                else:
                    grid[i][j] = max(grid[i][j + 1], grid[i + 1][j])

        return grid[0][0]


if __name__ == '__main__':
    solution = Solution()

    # Input: text1 = "abcde", text2 = "ace"
    # Output: 3
    print(solution.longestCommonSubsequence("abcde", "ace"))

    print(solution.longestCommonSubsequence("abde", "ace"))

    # Input: text1 = "abc", text2 = "abc"
    # Output: 3
    print(solution.longestCommonSubsequence("abc", "abc"))

    # Input: text1 = "abc", text2 = "def"
    # Output: 0
    print(solution.longestCommonSubsequence("abc", "def"))
