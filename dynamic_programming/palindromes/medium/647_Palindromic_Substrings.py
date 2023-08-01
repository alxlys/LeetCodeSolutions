# https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes_cnt = 0

        def helper(l, r):
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt

        for i in range(len(s)):
            palindromes_cnt += helper(i, i)
            palindromes_cnt += helper(i, i + 1)
        return palindromes_cnt


if __name__ == '__main__':
    solution = Solution()

    # Input: s = "abc"
    # Output: 3
    print(solution.countSubstrings('abc'))

    # Input: s = "aaa"
    # Output: 6
    print(solution.countSubstrings('aaa'))
