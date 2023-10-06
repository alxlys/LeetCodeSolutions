# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        _l, _r = 0, len(s) - 1

        while _l < _r:
            while not s[_l].isalnum() and _l < _r:
                _l += 1
            while not s[_r].isalnum() and _l < _r:
                _r -= 1
            if s[_l].lower() != s[_r].lower():
                return False
            _l += 1
            _r -= 1

        return True


if __name__ == '__main__':
    solution = Solution()

    # Input: s = "A man, a plan, a canal: Panama"
    # Output: true
    print(solution.isPalindrome('A man, a plan, a canal: Panama'))

    # Input: s = "race a car"
    # Output: false
    print(solution.isPalindrome('race a car'))

    # Input: s = " "
    # Output: true
    print(solution.isPalindrome(' '))

    print(solution.isPalindrome('0P'))
