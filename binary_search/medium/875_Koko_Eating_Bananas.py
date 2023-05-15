# https://leetcode.com/problems/koko-eating-bananas/description/
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r  # meaning max

        while l <= r:
            mid = (l + r) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / mid)
            if total_time <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: piles = [3, 6, 7, 11], h = 8
    # Output: 4
    print(solution.minEatingSpeed([3, 6, 7, 11], 8))

    # Input: piles = [30, 11, 23, 4, 20], h = 5
    # Output: 30
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 5))

    # Input: piles = [30, 11, 23, 4, 20], h = 6
    # Output: 23
    print(solution.minEatingSpeed([30, 11, 23, 4, 20], 6))
