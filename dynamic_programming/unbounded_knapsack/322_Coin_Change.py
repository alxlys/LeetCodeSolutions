# https://leetcode.com/problems/coin-change/
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # value won't be bigger
        default = amount + 1
        dp = [default] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != default else -1


if __name__ == '__main__':
    solution = Solution()

    # Input: coins = [1, 2, 5], amount = 11
    # Output: 3
    print(solution.coinChange([1, 2, 5], 11))

    # Input: coins = [2], amount = 3
    # Output: -1
    print(solution.coinChange([2], 3))

    # Input: coins = [1], amount = 0
    # Output: 0
    print(solution.coinChange([1], 0))
