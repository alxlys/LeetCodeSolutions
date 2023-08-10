# https://leetcode.com/problems/valid-palindrome-ii/

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def check_string(l: int, r: int, retry: bool) -> bool:
            while l < r:
                if s[l] != s[r]:
                    if retry:
                        return check_string(l + 1, r, False) or check_string(l, r - 1, False)
                    return False
                l += 1
                r -= 1
            return True

        return check_string(0, len(s) - 1, True)


if __name__ == '__main__':
    solution = Solution()

    # Input: s = "aba"
    # Output: true
    print(solution.validPalindrome('aba'))

    # Input: s = "abca"
    # Output: true
    print(solution.validPalindrome('abca'))

    # Input: s = "abc"
    # Output: false
    print(solution.validPalindrome('abc'))
