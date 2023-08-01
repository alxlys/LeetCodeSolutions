# https://leetcode.com/problems/longest-common-subsequence/
class Solution:
    # correct way of doing things with true DP bottom-up approach
    # Time: O(n * m), Space: O(n + m)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    grid[i][j] = grid[i + 1][j + 1] + 1
                else:
                    grid[i][j] = max(grid[i][j + 1], grid[i + 1][j])

        return grid[0][0]

    # more intuitive DFS + memorization solution
    def longestCommonSubsequence_dfs_memo(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        cache = [[-1] * len2 for _ in range(len1)]

        def dfs(i1: int, i2: int) -> int:
            if i1 == len1 or i2 == len2:
                return 0
            if cache[i1][i2] != -1:
                return cache[i1][i2]

            if text1[i1] == text2[i2]:
                cache[i1][i2] = 1 + dfs(i1 + 1, i2 + 1)
            else:
                cache[i1][i2] = max(dfs(i1 + 1, i2), dfs(i1, i2 + 1))
            return cache[i1][i2]

        return dfs(0, 0)


if __name__ == '__main__':
    solution = Solution()

    # Input: text1 = "abcde", text2 = "ace"
    # Output: 3
    print(solution.longestCommonSubsequence_dfs_memo("abcde", "ace"))

    print(solution.longestCommonSubsequence_dfs_memo("abde", "ace"))

    # Input: text1 = "abc", text2 = "abc"
    # Output: 3
    print(solution.longestCommonSubsequence_dfs_memo("abc", "abc"))

    # Input: text1 = "abc", text2 = "def"
    # Output: 0
    print(solution.longestCommonSubsequence_dfs_memo("abc", "def"))
