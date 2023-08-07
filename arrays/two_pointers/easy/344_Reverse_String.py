# https://leetcode.com/problems/reverse-string/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l += 1
            r -= 1


if __name__ == '__main__':
    solution = Solution()

    # Input: s = ["h", "e", "l", "l", "o"]
    # Output: ["o", "l", "l", "e", "h"]
    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)
    print(s)

    # Input: s = ["H", "a", "n", "n", "a", "h"]
    # Output: ["h", "a", "n", "n", "a", "H"]
    s = ["H", "a", "n", "n", "a", "h"]
    solution.reverseString(s)
    print(s)
