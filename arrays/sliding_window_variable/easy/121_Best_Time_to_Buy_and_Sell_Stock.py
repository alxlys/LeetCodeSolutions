# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                max_profit = max(max_profit, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return max_profit


if __name__ == '__main__':
    solution = Solution()

    # Input: prices = [7, 1, 5, 3, 6, 4]
    # Output: 5
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))

    # Input: prices = [7, 6, 4, 3, 1]
    # Output: 0
    print(solution.maxProfit([7, 6, 4, 3, 1]))

    # Input: [2, 1, 4]
    # Expected: 3
    print(solution.maxProfit([2, 1, 4]))
