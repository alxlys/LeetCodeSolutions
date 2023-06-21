# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        _l, _r = 0, len(s) - 1

        while _l < _r:
            if not s[_l].isalpha() and not s[_l].isalnum():
                _l += 1
                continue
            if not s[_r].isalpha() and not s[_r].isalnum():
                _r -= 1
                continue
            if s[_l].casefold() != s[_r].casefold():
                return False
            _l += 1
            _r -= 1

        return True


if __name__ == '__main__':
    solution = Solution()

    # Input: s = "A man, a plan, a canal: Panama"
    # Output: true
    # print(solution.isPalindrome('A man, a plan, a canal: Panama'))

    # Input: s = "race a car"
    # Output: false
    # print(solution.isPalindrome('race a car'))

    # Input: s = " "
    # Output: true
    # print(solution.isPalindrome(' '))

    print(solution.isPalindrome('0P'))
