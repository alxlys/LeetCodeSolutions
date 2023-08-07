# https://leetcode.com/problems/fruit-into-baskets/
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 1
        l = 0
        fruit_types = set()
        fruit_types.add(fruits[0])
        for r in (1, len(fruits)):
            if fruits[r] in




if __name__ == '__main__':
    solution = Solution()

    # Input: fruits = [1, 2, 1]
    # Output: 3
    print(solution.totalFruit([1, 2, 1]))

    # Input: fruits = [0, 1, 2, 2]
    # Output: 3
    print(solution.totalFruit([0, 1, 2, 2]))

    # Input: fruits = [1, 2, 3, 2, 2]
    # Output: 4
    print(solution.totalFruit([1, 2, 3, 2, 2]))
