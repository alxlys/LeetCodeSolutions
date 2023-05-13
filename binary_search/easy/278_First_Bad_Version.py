# https://leetcode.com/problems/first-bad-version/

bad = None


def isBadVersion(n: int) -> bool:
    if n >= bad:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    solution = Solution()

    # Input: n = 5, bad = 4
    # Output: 4
    bad = 4
    print(solution.firstBadVersion(5))

    bad = 1
    print(solution.firstBadVersion(1))
    # Input: n = 1, bad = 1
    # Output: 1
