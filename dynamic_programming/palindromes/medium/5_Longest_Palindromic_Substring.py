# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            max_palindrome = ''
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(max_palindrome):
                    max_palindrome = s[l:r + 1]
                l -= 1
                r += 1
            return max_palindrome

        max_total = ''
        for i in range(len(s)):
            max_curr = helper(i, i)
            if len(max_curr) > len(max_total):
                max_total = max_curr

            max_curr = helper(i, i + 1)
            if len(max_curr) > len(max_total):
                max_total = max_curr
        return max_total


if __name__ == '__main__':
    solution = Solution()

    # Input: s = "babad"
    # Output: "bab"
    print(solution.longestPalindrome('babad'))

    # Input: s = "cbbd"
    # Output: "bb"
    print(solution.longestPalindrome('cbbd'))
