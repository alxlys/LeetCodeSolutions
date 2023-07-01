# https://leetcode.com/problems/combinations/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        self.__helper__(1, [], combs, n, k)
        return combs

    def __helper__(self, i, curr_comb, combs, n, k):
        if len(curr_comb) == k:
            combs.append(curr_comb.copy())
            return
        if i > n:
            return
        for j in range(i, n + 1):
            curr_comb.append(j)
            self.__helper__(j + 1, curr_comb, combs, n, k)
            curr_comb.pop()


if __name__ == '__main__':
    solution = Solution()

    # Input: n = 4, k = 2
    # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    print(solution.combine(4, 2))

    # Input: n = 1, k = 1
    # Output: [[1]]
    print(solution.combine(1, 1))
