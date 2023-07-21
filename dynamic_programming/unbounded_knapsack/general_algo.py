def knapsack_01_dp(profit, weight, capacity):
    item_len, cap = len(profit), capacity
    dp = [[0] * (cap + 1) for _ in range(item_len)]

    # Actually it already contains 0's
    for i in range(item_len):
        dp[i][0] = 0
    # Filling first row with 1'st item weight
    for c in range(cap + 1):
        if weight[0] <= c:
            dp[0][c] = profit[0] * (c // weight[0])  # include item number of times we can

    for i in range(1, item_len):
        # row
        for c in range(1, cap + 1):
            # col
            # do not include current item
            skip = dp[i - 1][c]
            include = 0
            if c - weight[i] >= 0:
                # including current profit value and previous item in case if capacity allows
                include = profit[i] + dp[i][c - weight[i]]
            dp[i][c] = max(include, skip)
    return dp[item_len - 1][cap]


class Solution:

    # working but not memory optimized
    @staticmethod
    def knapsack_01_dp_mem(profit, weight, capacity):
        item_len, cap = len(profit), capacity
        dp = [0] * (cap + 1)

        # Filling first row with 1'st item weight
        for c in range(cap + 1):
            if weight[0] <= c:
                dp[c] = profit[0]

        for i in range(1, item_len):
            # row
            curr_row = [0] * (cap + 1)
            for c in range(1, cap + 1):
                # col
                # do not include current item
                skip = dp[c]
                include = 0
                if c - weight[i] >= 0:
                    # including current profit value and previous item in case if capacity allows
                    include = profit[i] + curr_row[c - weight[i]]
                curr_row[c] = max(include, skip)
            dp = curr_row
        return dp[cap]


if __name__ == '__main__':
    solution = Solution()

    # Input: profit = [4, 4, 7, 1], weight = [5, 2, 3, 1], capacity = 8
    # Output: 18
    print(solution.knapsack_01_dp_mem([4, 4, 7, 1], [5, 2, 3, 1], 8))
