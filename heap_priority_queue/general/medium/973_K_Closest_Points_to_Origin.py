# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        class Point:
            def __init__(self, distance, point):
                self.distance = distance
                self.point = point

            def __lt__(self, other):
                return self.distance < other.distance

        heap = []
        for point in points:
            heapq.heappush(heap, Point(point[0] * point[0] + point[1] * point[1], point))

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap).point)
        return res


if __name__ == '__main__':
    solution = Solution()

    # Input: points = [[1, 3], [-2, 2]], k = 1
    # Output: [[-2, 2]]
    print(solution.kClosest([[1, 3], [-2, 2]], 1))

    # Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
    # Output: [[3, 3], [-2, 4]]
    print(solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
