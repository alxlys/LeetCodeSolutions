# https://leetcode.com/problems/guess-number-higher-or-lower/

pick = None


def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution:

    def guessNumber(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            num = l + (r - l) // 2
            res = guess(num)
            if res == -1:
                r = num - 1
            elif res == 1:
                l = l + 1
            else:
                return num


if __name__ == '__main__':
    solution = Solution()

    # Input: n = 10, pick = 6
    # Output: 6
    pick = 6
    print(solution.guessNumber(10))

    # Input: n = 1, pick = 1
    # Output: 1
    pick = 1
    print(solution.guessNumber(1))

    # Input: n = 2, pick = 1
    # Output: 1
    pick = 1
    print(solution.guessNumber(2))
