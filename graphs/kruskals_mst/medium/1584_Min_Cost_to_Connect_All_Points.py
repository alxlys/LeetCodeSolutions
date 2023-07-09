# https://leetcode.com/problems/min-cost-to-connect-all-points/
import heapq
from typing import List


class Solution:
    class UnionFind:
        def __init__(self, n):
            self.par = {}
            self.rank = {}

            for i in range(0, n):
                self.par[i] = i
                self.rank[i] = 0

        def __find__(self, n):
            p = self.par[n]
            while p != self.par[p]:
                self.par[p] = self.par[self.par[p]]
                p = self.par[p]
            return p

        def union(self, n1, n2):
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

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = []
        N = len(points)
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(min_heap, [dist, i, j])

        union_find = self.UnionFind(N)
        mst = []
        res = 0
        while len(mst) < N - 1:
            dist, n1, n2 = heapq.heappop(min_heap)
            if not union_find.union(n1, n2):
                continue
            res += dist
            mst.append([n1, n2])
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    # Output: 20
    print(solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))

    # Input: points = [[3, 12], [-2, 5], [-4, 1]]
    # Output: 18
    print(solution.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]))
