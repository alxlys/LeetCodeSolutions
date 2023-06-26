# https://leetcode.com/problems/redundant-connection/
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.par = {}
        self.rank = {}

        for i in range(1, len(edges) + 1):
            self.par[i] = i
            self.rank[i] = 0

        for n1, n2 in edges:
            if not self.__union__(n1, n2):
                return [n1, n2]
        return []

    def __find__(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def __union__(self, n1, n2):
        p1, p2 = self.__find__(n1), self.__find__(n2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


if __name__ == '__main__':
    solution = Solution()

    # Input: edges = [[1, 2], [1, 3], [2, 3]]
    # Output: [2, 3]
    print(solution.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))

    solution = Solution()
    # Input: edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    # Output: [1, 4]
    print(solution.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
